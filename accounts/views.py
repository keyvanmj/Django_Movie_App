import json
from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView , PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Sum, Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView, RedirectView, DetailView, CreateView, TemplateView
from django.conf import settings

from Movie_app.forms import MovieImageForm
from Vote_app.models import Vote
from .decorators import ajax_login_required
from .mixins import AjaxTemplateMixin, AjaxFormMixin
from .models import Activation, Profile
from .utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from .forms import *


class GuestOnlyView(View):

    def dispatch(self, request, *args, **kwargs):
        # Redirect to the index page if the user already authenticated
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)


class LogInView(AjaxFormMixin,GuestOnlyView, FormView):
    template_name = 'accounts/log_in.html'

    @staticmethod
    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME or settings.LOGIN_VIA_EMAIL:
            return SignInViaEmailForm

        if settings.LOGIN_VIA_EMAIL_OR_USERNAME:
            return SignInViaEmailOrUsernameForm

        return SignInViaUsernameForm

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request

        # If the test cookie worked, go ahead and delete it since its no longer needed
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

        # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
        # the SESSION_COOKIE_AGE settings' option.
        if settings.USE_REMEMBER_ME:
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)

        login(request, form.user_cache)

        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))
        url_is_safe = is_safe_url(redirect_to, allowed_hosts=request.get_host(), require_https=request.is_secure())

        msg = f'successfully logged in as {self.request.user.username}'

        if url_is_safe:
            return self.ajax(success_message=msg)
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


class SignUpView(AjaxFormMixin,GuestOnlyView, FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        if settings.DISABLE_USERNAME:
            # Set a temporary username
            user.username = get_random_string()
        else:
            user.username = form.cleaned_data['username']

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        # Create a user record
        user.save()

        # Change the username to the "user_ID" form
        if settings.DISABLE_USERNAME:

            user.username = f'user_{user.id}'
            user.save()

        if settings.ENABLE_USER_ACTIVATION:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.save()

            send_activation_email(request, user.email, code)

            messages.success(
                request, _('You are signed up. To activate the account, follow the link sent to the mail.'))
        else:
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            msg = _('You are successfully signed up!')

            return self.ajax(success_message=msg)

        return redirect('Main:home')

class ActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Activate profile
        user = act.user
        user.is_active = True
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, _('You have successfully activated your account!'))

        return redirect('Main:home')


class ResendActivationCodeView(GuestOnlyView, FormView):
    template_name = 'accounts/resend_activation_code.html'

    @staticmethod
    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME:
            return ResendActivationCodeViaEmailForm

        return ResendActivationCodeForm

    def form_valid(self, form):
        user = form.user_cache

        activation = user.activation_set.first()
        activation.delete()

        code = get_random_string(20)

        act = Activation()
        act.code = code
        act.user = user
        act.save()

        send_activation_email(self.request, user.email, code)

        messages.success(self.request, _('A new activation code has been sent to your email address.'))

        return redirect('Accounts:resend_activation_code')


class RestorePasswordView(AjaxFormMixin,GuestOnlyView, FormView):
    template_name = 'accounts/restore_password.html'


    @staticmethod
    def get_form_class(**kwargs):
        if settings.RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME:
            return RestorePasswordViaEmailOrUsernameForm

        return RestorePasswordForm

    def form_valid(self, form):
        user = form.user_cache
        token = default_token_generator.make_token(user)
        # uid = urlsafe_base64_encode(force_bytes(user.pk)).encode()
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        if isinstance(uid,bytes):
            uid = uid.decode()
        # / accounts / restore / MTg / set - password /

        send_reset_password_email(self.request, user.email, token, uid)
        msg = _('Email has been sent')
        return self.ajax(success_message=msg)

        # return redirect('Accounts:restore_password_done')


class ChangeProfileView(LoginRequiredMixin, FormView):
    template_name = 'accounts/profile/change_profile.html'
    form_class = ChangeProfileForm
    login_url = '/'

    def get_login_url(self):
        """
        Override this method to override the login_url attribute.
        """
        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                '{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL, or override '
                '{0}.get_login_url().'.format(self.__class__.__name__)
            )
        return str(login_url)



    def get_initial(self):
        user = self.request.user
        initial = super().get_initial()
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['image'] = user.profile.image
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.profile.image = form.cleaned_data['image']
        user.save()

        messages.success(self.request, _('Your profile has been updated !'))
        return redirect('Accounts:change_profile')



    def get_context_data(self, **kwargs):
        context = super(ChangeProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        like_obj = Vote.objects.filter(user=self.request.user,value=1)
        dislike_obj = Vote.objects.filter(user=self.request.user,value=-1)
        context['like_obj'] = [(x.movie if x.movie else x.series) for x in like_obj]
        context['dislike_obj'] = [(x.movie if x.movie else x.series) for x in dislike_obj]
        return context




class ChangeEmailView(AjaxFormMixin,LoginRequiredMixin, FormView):
    template_name = 'accounts/profile/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data['email']

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.email = email
            act.save()

            send_activation_change_email(self.request, email, code)

            messages.success(self.request, _('To complete the change of email address, click on the link sent to it.'))
        else:
            user.email = email
            user.save()


        return self.ajax(success_message=_('Changing Email ...'))


class ChangeEmailActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Change the email
        user = act.user
        user.email = act.email
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, _('You have successfully changed your email!'))

        return redirect('Accounts:change_email')


class RemindUsernameView(AjaxFormMixin,GuestOnlyView, FormView):
    template_name = 'accounts/remind_username.html'
    form_class = RemindUsernameForm

    def form_valid(self, form):
        user = form.user_cache
        send_forgotten_username_email(user.email, user.username)
        request = self.request
        success_msg = _('Your username has been successfully sent to your email.')
        return self.ajax(success_message=success_msg)


class ChangePasswordView(AjaxFormMixin,BasePasswordChangeView):
    template_name = 'accounts/profile/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, _('Your password was changed.'))

        return self.ajax(success_message='Changing Password ...')


class RestorePasswordConfirmView(AjaxFormMixin,BasePasswordResetConfirmView):
    template_name = 'accounts/restore_password_confirm.html'

    def form_valid(self, form):
        # Change the password
        form.save()

        success_msg = _('Your password has been set. You may go ahead and login now.')

        return self.ajax(success_message=success_msg,success_url=reverse('Main:home'))


class RestorePasswordDoneView(BasePasswordResetDoneView):
    template_name = 'accounts/restore_password_done.html'

    def __str__(self):
        return super(RestorePasswordDoneView, self).__str__()

    def get_context_data(self, **kwargs):
        if 'RestorePasswordDoneView' in self.__str__():
            print('yes')
        else:
            print('no ')
        return super(RestorePasswordDoneView, self).get_context_data(**kwargs)


class LogOutView(LogoutView,LoginRequiredMixin):

    def get(self, request,*args,**kwargs):
        logout(request)
        return redirect('/')




def redirect_login_url(request):
    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False
    context = {
        'is_authenticated':is_authenticated,
    }
    return JsonResponse(context)