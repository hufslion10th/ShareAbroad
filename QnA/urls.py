from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'QnA'

urlpatterns = [
    path('', views.question_list, name='index'),#TODO 없애기
    path('create-Q', views.create_question, name='create-Q'),
    path('create-A/<int:pk>', views.create_answer, name='create-A'),
    path('list', views.question_list, name='QnA-list'),
    path('detail/<int:pk>', views.question_detail, name='QnA-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
