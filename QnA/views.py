from django.shortcuts import render, redirect
from .models import *
from users.models import *
from .forms import *

# 질문글 작성 view
def create_question(request):
    # POST 요청이면 작성된 질문 폼을 처리한다.
    if request.method == 'POST':

        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다.
        question_form = CreateQuestionForm(request.POST, request.FILES)

        # 폼이 유효한지(모든 값이 들어있는지) 체크한다:
        if question_form.is_valid():
            question = question_form.save(commit=False)
            #작성자를 추가해준다.(이 부분은 후에 로그인 기능 만들고 수정할 예정)
            question.writer = User.objects.get(id=1)
            #질문 글을 저장한다.
            question.save()

            # 새로운 URL로 보낸다:
            return redirect('QnA:QnA-detail', question.pk)

    # GET 요청 (혹은 다른 메소드)이면 기본 폼을 생성한다.
    else:
        question_form = CreateQuestionForm() #forms.py에 만들어두고 가져옴
    ctx = {
        'question_form': question_form,
    }

    return render(request, template_name='QnA/questionCreate.html', context=ctx)


def create_answer(request, pk):
    question = QuestionPost.objects.get(id=pk)

    if request.method == 'POST':
        answer_form = CreateAnswerForm(request.POST, request.FILES)

        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.writer = User.objects.get(id=1)
            answer.save()
            return redirect('QnA:QnA-detail', question.pk)

    else:
        answer_form = CreateAnswerForm()
    ctx = {
        'question': question,
        'answer_form': answer_form,
    }
    return render(request, template_name='QnA/answerCreate.html', context=ctx)


# 질문글 하나만 보는 view
def question_detail(request, pk):
    question = QuestionPost.objects.get(id=pk)

    ctx = {
        "question": question,
    }
    return render(request, template_name='QnA/detail.html', context=ctx)


# 질문들 리스트 게시판 보는 view
def question_list(request):
    questions = QuestionPost.objects.all()

    ctx = {
        "questions": questions,
    }
    return render(request, template_name='QnA/list.html', context=ctx)
