from django.urls import path, include
from .import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.UserProfileViewset )



urlpatterns = [
    path("hello/",views.HelloAPIView.as_view(), name="hello"),
    path("", include(router.urls)),

]

#the Difference between APIView and ViewSets is that ViewSets are automatically creating the urls using routing
#APIView is manually creating the urls

#APIView more flexibile to control logics
#ViewSets are automatic for simple CRUD with no need to manually control the CRUD