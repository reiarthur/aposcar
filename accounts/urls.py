from django.urls import path, re_path
from .views import *

app_name = 'accounts'
urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(), name="login"),
    re_path(r'^signup/$', RegisterView.as_view(), name="signup"),
    re_path(r'^logout/$', LogoutView.as_view(), name="logout")
]