from Vote_app.models import Rate
from accounts.forms import SignInViaEmailOrUsernameForm

def add_my_login_form(request):
    return {
        'login_form_context': SignInViaEmailOrUsernameForm(),
    }



