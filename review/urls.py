from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'review'

urlpatterns = [
    path('', views.review_list, name='review-list'),
    path('create', views.create_review, name='create-R'),
    path('list', views.review_list, name='review-list'),
    path('detail/<int:pk>', views.review_detail, name='review-detail'),
    #path('delete/<int:pk>', views.review_delete, name="review-delete"), # 삭제 기능
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
