from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hola mundo. Tu estas en el index de polls")

def detail(request, question_id):
    return HttpResponse("Estas mirando una respuesta %s." % question_id)

def results(request, question_id):
    response = "Estas mirando los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s." % question_id)