from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("This is index page")


def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking at response of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting for the question {question_id}")
