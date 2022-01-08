from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.encoding import force_text
from django.utils.http import is_safe_url
from django.views.generic.base import ContextMixin


class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            # split template_name
            split = self.template_name.split('.html')
            # add _inner to the end of split list
            split[-1] = '_inner'
            # add .html to the split list
            split.append('.html')
            # join split list without spaces
            self.ajax_template_name = ''.join(split)
        # ajax_template_name defaults to template_name_inner.html
        # if the request is AJAX, then the view renders this template
        # otherwise, the view renders the template_name.html template
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)



class AjaxFormMixin(ContextMixin):


    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        request = self.request

        if request.is_ajax:
            return JsonResponse({'form_error':form.errors})
        else:
            return response

    def get_success_url(self):
        request = self.request
        nxt = request.GET.get("next", None)
        if nxt is None:
            return redirect(request.META['HTTP_REFERER'])
        elif not is_safe_url(
                url=nxt,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure()):
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(nxt)

    def ajax(self,success_message=None,success_url=None,*args,**kwargs):
        if self.request.is_ajax:
            try:
                next_params = f"/{self.get_success_url().url.split('?next=/')[1]}"
            except:
                next_params = ''

            return JsonResponse({
                'success':success_message,
                'redirect_to':  self.get_success_url().url if success_url is None else success_url,
                'next_url':next_params
            })
