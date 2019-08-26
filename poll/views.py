from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ems.decorators import admin_hr_required,admin_only
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.edit import CreateView
from poll.form import PollForm, ChoiceForm



class PollView(View):
    decorators = [login_required, admin_hr_required ]

    @method_decorator(decorators)
    def get(self, request, id=None):
        if id:
            question = get_object_or_404(Question, id=id)
            poll_form = PollForm(instance=question)
            choices = question.choice_set.all()
            choice_forms = [ChoiceForm(prefix=str(
                choice.id), instance=choice) for choice in choices]
            template = 'poll/edit_poll.html'
        else:
            poll_form = PollForm(instance=Question())
            choice_forms = [ChoiceForm(prefix=str(
                x), instance=Choice()) for x in range(3)]
            template = 'poll/new_poll.html'
        context = {'poll_form': poll_form, 'choice_forms': choice_forms}
        return render(request, template, context)


    @method_decorator(decorators)
    def post(self,request,id=None):
        context = {}
        if id:
            self.put(request)
        poll_form = PollForm(request.POST, instance=Question())
        choice_form = [ChoiceForm(request.POST,prefix=str(x),instance=Choice())for x in range(0,3)]
        if poll_form.is_valid and all([cf.is_valid for cf in choice_form]):
            new_poll = poll_form.save(commit=False)
            new_poll.Created_by = request.user
            new_poll.save()
            for cf in choice_form:
                new_choice = cf.save(commit=False)
                new_choice.quetions = new_poll
                new_choice.save()
            return HttpResponseRedirect('/polls/list/')

        context = {'poll_form': poll_form, 'choice_forms': choice_form}
        return render(request, 'polls/new_poll.html', context)


    @method_decorator(decorators)
    def put(self, request, id=None):
        context = {}
        question = get_object_or_404(Question, id=id)
        poll_form = PollForm(request.POST, instance=question)
        print(question.choice_set.all)
        choice_forms = [ChoiceForm(request.POST, prefix=str(
            choice.id), instance=choice) for choice in question.choice_set.all()]
        if poll_form.is_valid() and all([cf.is_valid() for cf in choice_forms]):
            new_poll = poll_form.save(commit=False)
            new_poll.Created_by = request.user
            new_poll.save()
            print(question.Title)
            for cf in choice_forms:
                new_choice = cf.save(commit=False)
                new_choice.question = new_poll
                new_choice.save()
            return redirect('polls_list')
        context = {'poll_form': poll_form, 'choice_forms': choice_forms}
        return render(request, 'polls/edit_poll.html', context)


    @method_decorator(decorators)
    def delete(self, request, id=None):
        question = get_object_or_404(Question)
        question.delete()
        return redirect('polls_list')


@login_required(login_url="/login/")
    
def index(request):
    
    context = {}
    questions = Question.objects.all()
    context['little'] = 'poll'
    context['questions'] = questions
    return render(request, 'poll/index.html', context)

@login_required(login_url="/login/")
def details(request,id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    print('choices are : ',question.choices, question.Title,question.Created_by.first_name)
    return render(request, 'poll/details.html', context)

#if url is http://127.0.0.1:8000/polls/4/ then get the page 
@login_required(login_url="/login/")
def poll(request,id=None):
    if request.method == "GET" :
        context = {}
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context['question'] = question
        print('choices are : ',question.choices)
        return render(request, 'poll/poll.html', context)

#if user post any data in this page 
    if request.method == "POST":
        user_id = 1
        print(request.POST)
        data = request.POST
        print('data is : ',data)
        ret = Answer.objects.create(user_id = user_id, choice_id = data['choice'])
        if ret:
            return HttpResponse('Your vote is done succesfully')
        else:
            return HttpResponse('Your vote is not done succesfully')


