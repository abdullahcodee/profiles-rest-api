from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")


urlpatterns = [
    path("hello/",views.HelloAPIView.as_view(), name="hello"),
    path("", include(router.urls)),


]
