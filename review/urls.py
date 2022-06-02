from django.urls import path
from . import views


app_name = 'review'

urlpatterns = [
    path('', views.review),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
