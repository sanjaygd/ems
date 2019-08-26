from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
from employee.form import UserForms
from django.http import HttpResponseRedirect,HttpResponse
from ems.decorators import admin_only


def profile(request):
    pass



def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context['error'] = 'Please provide the valied credential!'
            return render(request, 'authentication/login.html', context)
    else:
        return render(request, "authentication/login.html", context)


@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'authentication/success.html', context)

# must not use this decorator here It won't allow to go back login page @login_required(login_url="/login/")
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
def employe_list(request):
        context = {}
        context['users'] = User.objects.all()
        context['title'] = 'Employees'
        context['little'] = 'Employees'
        return render (request, 'employee/index.html', context)


@login_required(login_url="/login/")
def employe_details(request,id=None):
    context = {}
    context['user'] = get_object_or_404(User,id=id)
    print('context  of employee details is : ',context)
    return render(request, 'employee/details.html', context)


@login_required(login_url="/login/")
# @role_required(allowed_role = ['Admin'])
@admin_only
def employee_add(request):
    # if request.role =="Admin":   if I add this condition other than Admin no one can access add page
    context = {}
    if request.method == 'POST':
        user_form = UserForms(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', context)
    else:
        user_form = UserForms()
        context['user_form']= user_form
        print(context)
        return render(request, 'employee/add.html', context)
        

@login_required(login_url="/login/")
def employe_edit(request,id=None):
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        user_form = UserForms(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/edit.html', {'user_form':user_form})
    else:
        user_form = UserForms(instance = user)
        return render(request, 'employee/edit.html', {'user_form':user_form})


@login_required(login_url="/login/")
def employe_delete(request,id=None):
    #user = get_object_or_404(User,id=id)
    user = User.objects.get(id=id)
    print('delete user is :',user)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        conext = {}
        conext['user'] = user
        print(conext)
        return render(request, 'employee/delete.html', conext)
    

class ProfileUpdate(UpdateView):
    fields = ['Designation', 'salary']
    template_name = 'authentication/profile_update.html'
    success_url = reverse_lazy('my_profile')


    def get_object(self):
        return self.request.user.profile




class MyProfile(DetailView):
    template_name = 'authentication/profile.html'
    
    def get_object(self):
        return self.request.user.profile