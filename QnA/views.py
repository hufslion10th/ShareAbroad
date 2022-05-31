from django.shortcuts import render, redirect
from .models import *
from users.models import *
from .forms import *


def create_question(request):
    # POST 요청이면 폼 데이터를 처리한다
    if request.method == 'POST':

        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다 (binding):
        question_form = CreateQuestionForm(request.POST, request.FILES)

        # 폼이 유효한지 체크한다:
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.writer = User.objects.get(id=1)
            question.save()

            # 새로운 URL로 보낸다:
            return redirect('QnA:QnA-detail', question.pk)

    # GET 요청 (혹은 다른 메소드)이면 기본 폼을 생성한다.
    else:
        question_form = CreateQuestionForm()
    ctx = {
        'question_form': question_form,
    }

    return render(request, template_name='QnA/questionCreate.html', context=ctx)


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
