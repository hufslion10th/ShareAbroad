from django.contrib import admin
from django.urls import path, include
from . import views #민혁추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home), #민혁추가
    path('QnA/', include('QnA.urls', namespace="QnA")),
    path('users/', include('users.urls', namespace="users")),
    path('review/', include('review.urls', namespace="review")),
]
