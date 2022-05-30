from django.shortcuts import render
from .models import *


def create_question(request):
    return render(request, template_name='QnA/questionCreate.html')


def create_answer(request):
    return render(request, template_name='QnA/answerCreate.html')


def question_detail(request, pk):
    question = QuestionPost.objects.get(id=pk)

    ctx = {
        "question": question,
    }
    return render(request, template_name='QnA/detail.html', context=ctx)


def question_list(request):
    questions = QuestionPost.objects.all()

    ctx = {
        "questions": questions,
    }
    return render(request, template_name='QnA/list.html', context=ctx)
