from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username',
                  'password']
        # excludes = ['']
        
        label = {
            'password': 'Password'
        }

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.                
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)


    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])

        u.set_password(password)
        u.save()
        return u


"""from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User,Group

class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                    'email', 'username',
                    'password']

        # exlcude =['']

        label = {
            'password':'Password'
        }



        def __init__(self, *args, **kwargs):
            if kwargs.get('instance'):
                #we get the initial keyword argument or initialize it
                #as a dict it didn't exist
                initial = kwargs.setdefault('initial',{})
                #the widget for a ModelMultipleFiel expects
                #A list of primary key for selected data
                if kwargs['instance'].Group.all():
                    initial['role'] = kwargs['instance'].Group.all()[0]
                else:
                    initial['role'] = None

            forms.ModelForm.__init__(self,*args,**kwargs)


        # def clean_email(self):
        #     if self.cleaned_data['email'].endsWith('@gmail.com'):
        #         return self.cleaned_data['email']
        #     else:
        #         raise ValidationError('Email is not valied')

        def save(self):
            password = self.cleaned_data.pop('password')
            role = self.cleaned_data.pop('role')
            u = super().save()
            u.set_password(password)
            u.groups.set([role])
            u.save()
            return u
"""