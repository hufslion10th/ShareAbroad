from django.db import models
from users.models import *
from .enums import *

class ReviewPost(models.Model):
    title = models.CharField(max_length=20, verbose_name="리뷰 제목")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="리뷰 작성자") #TODO on_delete 다시 설정
    content = models.TextField(verbose_name="리뷰 내용")
    category = models.CharField(max_length=15, choices=ReviewCategory.choices, verbose_name="리뷰 카테고리")
    like = models.PositiveSmallIntegerField(null=True, default=0, verbose_name="리뷰 좋아요 수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.writer}의 리뷰 : {self.title}" # admin에서 보기 편하게 하려고

    class Meta: # admin에서 보기 편하게 하려고
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"

    
class ReviewPhoto(models.Model):
    review = models.ForeignKey(ReviewPost, on_delete=models.CASCADE, verbose_name="리뷰글")
    photo = models.ImageField(upload_to='question/', null=True, blank=True, verbose_name="리뷰 사진")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.review.title}의 사진"

    class Meta:
        verbose_name = "리뷰 사진"
        verbose_name_plural = "리뷰 사진"


class ReviewComment(models.Model):
    review = models.ForeignKey(ReviewPost, on_delete=models.CASCADE, verbose_name="리뷰 댓글")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="리뷰 댓글 작성자")
    content = models.TextField(verbose_name="질문 댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")

    def __str__(self):
        return f"{self.writer}의 {self.review.title}에 대한 댓글"

    class Meta:
        verbose_name = "리뷰 댓글"
        verbose_name_plural = "리뷰 댓글"
