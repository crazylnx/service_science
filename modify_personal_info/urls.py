from django.urls import path
from .views import *

from django.conf import settings
app_name='modify_personal_info'
urlpatterns = [
    path('<str:name>/', personal_view, name='PersonalView'),
    path('<str:name>/<int:value>', reward, name='Reward'),
]