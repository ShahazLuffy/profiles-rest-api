from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api-viewset', HelloViewSet, base_name='api-viewset')

urlpatterns = [
    path('hello_view/', HelloApiView.as_view()),
    path('', include(router.urls))

]
