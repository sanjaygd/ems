from django import forms
from poll.models import Question,Choice


class PollForm(forms.ModelForm):
    Title = forms.CharField(max_length=255, label='Question')  #made mistake here Title was wrongly typed as title results one more title column in html page

    class Meta:
        model = Question
        fields = ['Title']


class ChoiceForm(forms.ModelForm):
    text = forms.CharField(max_length=255, label='Choice')


    class Meta:
        model = Choice
        exclude = ['quetions']

