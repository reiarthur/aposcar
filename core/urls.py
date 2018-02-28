from django.urls import path, re_path
from .views import *

app_name = 'core'
urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name="index"),
    re_path(r'^bets/create$', CreateBets.as_view(), name="create_bets"),
    re_path(r'^bets/$', ListBet.as_view(), name="list_bet"),
]