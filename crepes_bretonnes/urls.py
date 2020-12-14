from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog1/', include('blog.urls')),
]
