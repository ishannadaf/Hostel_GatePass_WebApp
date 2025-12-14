from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def role_required(role):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.role == role:
                return view_func(request, *args, **kwargs)
            return redirect('login')
        return wrapper
    return decorator
