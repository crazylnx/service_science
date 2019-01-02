from django.urls import path
from my_browsing_history.views import *
from django.conf import settings
app_name = 'my_browsing_history'
urlpatterns = [
    path('MyBrowsingHistory/', MyBrowsingHistory, name='mybrowsinghistory'),
    path('MyBrowsingHistory/Inner_IBrowsed', MyBrowsingHistoryInner, name='mybrowsinghistoryinner'),
    # path()
]