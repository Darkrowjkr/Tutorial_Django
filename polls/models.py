import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    user = models.CharField(max_length=60) 
    def __str__(self):
        return self.question_text

    def votes(self):
        suma = 0
        for choice in self.choice_set.all():
            suma += choice.votes
        return suma

    def choices(self):
        ctxt_list = []
        cvts_list = []
        for choice in self.choice_set.all():
            ctxt_list.append(choice.choice_text)
            cvts_list.append(choice.votes)
        return ctxt_list, cvts_list

    def last_day_question(self):
        qlist = []
        for q in Question.objects.all():
            if q.pub_date > (timezone.now() - datetime.timedelta(days=1)):
                qlist.append(q)
        return qlist

    #Se debe importar el admin de django.contrib
    @admin.display( 
        boolean=True,
        ordering='pub_date',
        description='Published recently',
    )
    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text