from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question

from django.shortcuts import render


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question_detail = Question.objects.get(pk=question_id)
        context = {"question": question_detail}
    except Question.DoesNotExist:
        raise Http404("Question does not exists!!")
    return render(request, "polls/details.html", context)


def results(request, question_id):
    return HttpResponse(f"You are looking at response of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting for the question {question_id}")
