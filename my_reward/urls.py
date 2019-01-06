from django.urls import path
from my_reward.views import *
app_name='my_reward'
urlpatterns = [
    path('recharge/',popup, name='recharge'),
]