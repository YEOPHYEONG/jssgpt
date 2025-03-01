"""
URL configuration for jssgpt_project project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin 페이지 URL
    path('user-experience/', include('user_experience.urls')),  # 앱의 URL 연결
    path('langchain/', include('langchain_app.urls')),  # langchain_app의 URL
    path('cover-letter/', include('user_coverletter.urls')),  # user_coverletter 앱의 URL 연결
    path('auth/', include('authentication.urls')),  # 소셜 로그인
]
