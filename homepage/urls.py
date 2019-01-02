from django.urls import path
from homepage.views import *
app_name='homepage1'
urlpatterns = [
     path('homepage/', homepage_view, name='homepage'),
     path('homepage/inner/',HomepageInner,name='homepageinner')
]