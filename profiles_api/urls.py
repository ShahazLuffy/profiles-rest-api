from django.urls import path, include
from .views import *

urlpatterns = [

    path('hello_view/', HelloApiView.as_view()),

]
