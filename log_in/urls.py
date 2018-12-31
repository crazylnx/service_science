from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('',views.login_view),
    path('login/', views.login,name='login'),
    path('rigister_view/', views.register_view, name='rigister'),
    path('rigister/',views.register)
]