from django.shortcuts import render
from review.models import *

def home(request):  # 민혁추가함. 
    reviews = ReviewPost.objects.all()

    ctx = {
        "reviews": reviews,
        "extra_sorting": ['최신 순', '조회 순', '공감 많은 순', '댓글 많은 순'],
    }
    return render(request, template_name='review/list.html', context=ctx)