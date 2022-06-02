from django import forms
from django.forms import ModelForm
from .models import *

class CreateReviewForm(ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'category', 'content', ]