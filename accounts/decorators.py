from functools import wraps
from django.http import JsonResponse
from django.shortcuts import redirect



def admin_required(func):
    @wraps(func)
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return func(request,*args,**kwargs)
        return redirect('/')
    return wrapper


def ajax_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            if request.is_ajax:
                if request.GET == None or request.GET == '' or request.GET == {}:
                    return redirect('/')
                data = {
                    'is_authenticated': False,
                    'url_path':request.path_info,
                    }
                return JsonResponse(data)
        return view_func(request, *args, **kwargs)
    return wrapper



