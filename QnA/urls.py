from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'QnA'

urlpatterns = [
    path('create-Q', views.create_question, name='create-Q'),
    path('create-A/<int:pk>', views.create_answer, name='create-A'),
    path('create-Qcomment-ajax/<int:pk>', views.create_comment_of_Q, name='create_comment_of_Q'),
    # path('create-Acomment-ajax/<int:pk>', views.create_comment_of_A, name='create_comment_of_A'),
    path('list', views.question_list, name='QnA-list'),
    path('detail/<int:pk>', views.question_detail, name='QnA-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
