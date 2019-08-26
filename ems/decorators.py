from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied


# def role_required(allowed_role=[]):
#     def decorator(view_fun):
#         def wrap(request, *args, **kwargs):
#             if request.role in allowed_role:
#                 return view_fun(request,*args,**kwargs)
#             else:
#                 return HttpResponseRedirect(reverse('employee_list'))
#         return wrap
#     return decorator


def admin_hr_required(view_fun):
        def wrap(request, *args, **kwargs):
            allowed_roles = ["Admin","HR"]
            if request.role in allowed_roles:
                return view_fun(request,*args,**kwargs)
            else:
                return KeyError 
                    
        return wrap



def admin_only(view_fun):
        def wrap(request, *args, **kwargs):
            if request.role == "Admin":
                return view_fun(request,*args,**kwargs)
            else:
                return HttpResponseRedirect(reverse('employee_list'))
        return wrap
    