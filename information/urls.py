from django.urls import path, include # include 민혁추가
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'

urlpatterns = [
    path('', views.information), # 기존에 이것만 있었음
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
