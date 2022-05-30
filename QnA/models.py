from django.db import models
from users.models import *
from .enums import *

class QuestionPost(models.Model):
    title = models.CharField(max_length=20, verbose_name="질문 제목")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="질문 작성자") #TODO on_delete 다시 설정
    content = models.TextField(verbose_name="질문 내용")
    category = models.CharField(max_length=15, choices=QuestionCategory.choices, verbose_name="질문 카테고리")
    like = models.PositiveSmallIntegerField(null=True, default=0, verbose_name="질문 좋아요 수")
    picked_answer = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="채택한 답변의 id")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.writer}의 질문 : {self.title}"

    class Meta:
        verbose_name = "질문"
        verbose_name_plural = "질문"


class AnswerPost(models.Model):
    question = models.ForeignKey(QuestionPost, on_delete=models.CASCADE, verbose_name="질문글")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="답변 작성자")
    content = models.TextField(verbose_name="답변 내용")
    picked = models.BooleanField(default=False, verbose_name="답변 채택 여부")
    like = models.PositiveSmallIntegerField(null=True, default=0, verbose_name="답변 좋아요 수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.writer}의 {self.question.title}에 대한 답변"

    class Meta:
        verbose_name = "답변"
        verbose_name_plural = "답변"


class QuestionPhoto(models.Model):
    question = models.ForeignKey(QuestionPost, on_delete=models.CASCADE, verbose_name="질문글")
    photo = models.ImageField(upload_to='question/', null=True, blank=True, verbose_name="질문 사진")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.question.title}의 사진"

    class Meta:
        verbose_name = "질문 사진"
        verbose_name_plural = "질문 사진"


class QuestionComment(models.Model):
    question = models.ForeignKey(QuestionPost, on_delete=models.CASCADE, verbose_name="질문 댓글")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="질문 댓글 작성자")
    content = models.TextField(verbose_name="질문 댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.writer}의 {self.question.title}에 대한 댓글"

    class Meta:
        verbose_name = "질문 댓글"
        verbose_name_plural = "질문 댓글"


class AnswerComment(models.Model):
    answer = models.ForeignKey(AnswerPost, on_delete=models.CASCADE, verbose_name="답변 댓글")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="답변 댓글 작성자")
    content = models.TextField(verbose_name="답변 댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.writer}의 {self.answer.content}에 대한 댓글"

    class Meta:
        verbose_name = "답변 댓글"
        verbose_name_plural = "답변 댓글"
