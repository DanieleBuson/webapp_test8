"""
URL configuration for webapp_test8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from skaaltec_test8 import views

urlpatterns = [
    path('admin_skaaltec_test_8/', admin.site.urls),


    path('', views.main, name='main'),
    path('solutions/', views.solutions, name='solutions'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)