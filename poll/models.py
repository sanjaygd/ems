from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    Title = models.TextField(null=True, blank=True)
    Status = models.CharField(default='Inactive',max_length=20)
    Created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) #made mistake here, models.CASCADE writen in string like this 'models.CASCADE'
    created_at = models.DateField(auto_now_add=True)  #once we created the object teh date of the object can not be changed
    update_at = models.DateField(auto_now = True,)   #It is just like showing last modified date

    def __str__(self):
        return self.Title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    quetions = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True,blank=True,null=True)
    update_at = models.DateField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.text

    @property
    def vote(self):
        return self.answer_set.count()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True,blank=True,null=True)
    update_at = models.DateField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text


    