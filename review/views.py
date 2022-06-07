from django.shortcuts import render, redirect
from .models import *
from users.models import *
from .forms import *

def review(request):
    return render(request, 'review/review.html')

# 리뷰글 작성 view
def create_review(request):
    # POST 요청이면 작성된 질문 폼을 처리한다.
    if request.method == 'POST':

        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다.
        review_form = CreateReviewForm(request.POST, request.FILES)

        # 폼이 유효한지(모든 값이 들어있는지) 체크한다:
        if review_form.is_valid():
            review = review_form.save(commit=False)
            #작성자를 추가해준다.(이 부분은 후에 로그인 기능 만들고 수정할 예정)
            review.writer = User.objects.get(id=1)
            #질문 글을 저장한다.
            review.save()

            # 새로운 URL로 보낸다:
            return redirect('review:review-detail', review.pk)

    # GET 요청 (혹은 다른 메소드)이면 기본 폼을 생성한다.
    else:
        review_form = CreateReviewForm() #forms.py에 만들어두고 가져옴
    ctx = {
        'review_form': review_form,
    }

    return render(request, template_name='review/create.html', context=ctx)


# 수정하기 
def edit_review(request, pk):
    review = ReviewPost.objects.get(id=pk)
    
    if request.method == 'POST':
        review.title = request.POST['title']
        review.category = request.POST['category']
        review.content = request.POST['content']

        review.save()
        return redirect('review:review-detail', review.pk)
    
    else:
        review_form = CreateReviewForm()

        ctx = {
            'review_form': review_form,
        }

        return render(request, template_name='review/reviewCreate.html', context=ctx)

# 삭제하기
def delete_review(request, pk):
    review = ReviewPost.objects.get(id=pk)

    review.delete()
    return redirect('review:review-list')


# 리뷰글 하나만 보는 view
def review_detail(request, pk):
    review = ReviewPost.objects.get(id=pk)

    ctx = {
        "review": review,
    }
    return render(request, template_name='review/detail.html', context=ctx)


# 리뷰들 리스트 게시판 보는 view
def review_list(request):
    reviews = ReviewPost.objects.all()

    ctx = {
        "reviews": reviews,
        "extra_sorting": ['최신 순', '조회 순', '공감 많은 순', '댓글 많은 순'],
    }
    return render(request, template_name='review/list.html', context=ctx)


# 리뷰글 삭제 view (민혁 추가)
'''def review_delete(request):
    reviews = ReviewPost.objects.all()
    ctx = {
        "reviews": reviews,
    }
    return render(request, template_name='review/list.html', context=ctx)'''