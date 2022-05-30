from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('QnA/', include('QnA.urls')),
    path('users/', include('users.urls')),
    path('information/', include('information.urls')),
    path('review/', include('review.urls')),
]
