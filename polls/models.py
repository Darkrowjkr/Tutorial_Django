import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
import base64

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
        for choice in self.choice_set.all():
            ctxt_list.append(choice.choice_text +" con %i votos" % choice.votes)
        return ctxt_list

    def last_day_question(self):
        qlist = []
        for q in Question.objects.all():
            if q.pub_date > (timezone.now() - datetime.timedelta(days=1)):
                qlist.append(q)
        return qlist

    def base64code(mensaje:str):
        message_bytes = mensaje.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    def base64decode(codigo:str):
        base64_bytes = codigo.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        message:int
        return message


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