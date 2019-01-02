"""service_science URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log_in.urls')),
    path('', include('homepage.urls')),
    path('', include('my_comments.urls')),
    path('', include('my_browsing_history.urls')),
    path('', include('show_question.urls')),
    # url(r'^administrator/', include('administrator.urls')),
    # url(r'^', include('homepage.urls')),
    # url(r'^log_in/', include('log_in.urls')),
    # url(r'^modify_personal_info/', include('modify_personal_info.urls')),
    # url(r'^my_browsing_history/', include('my_browsing_history.urls')),
    # url(r'^my_comments/', include('my_comments.urls')),
    # url(r'^my_reward/', include('my_reward.urls')),
    
]
