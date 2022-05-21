from django.urls import path
from .views import *

urlpatterns = [
    path("chat/<int:pk>", ProfileAddMessage.as_view(), name="chat"),
    path('', index, name="home"),
    path('accounts', accounts, name="accounts"),
]
