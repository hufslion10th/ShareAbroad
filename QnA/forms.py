from django import forms
from django.forms import ModelForm
from .models import *

class CreateQuestionForm(ModelForm):
    class Meta:
        model = QuestionPost
        fields = ['title', 'category', 'content', ]


class CreateAnswerForm(ModelForm):
    class Meta:
        model = AnswerPost
        fields = ['content', ]
