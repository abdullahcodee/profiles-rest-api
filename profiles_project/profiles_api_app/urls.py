from django.urls import path, include
from .import views
from rest_framework.authtoken.views import ObtainAuthToken


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.UserProfileViewset )
router.register("feed", views.UserProfileFeedViewSet) #if it's inherted from viewset it doesn't require basename


"""we use the base name if it's not a modelViewSet to make django identify the router"""




urlpatterns = [
    path("hello/",views.HelloAPIView.as_view(), name="hello"),
    path('login/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path("", include(router.urls)),

]

#the Difference between APIView and ViewSets is that ViewSets are automatically creating the urls using routing
#APIView is manually creating the urls

#APIView more flexibile to control logics
#ViewSets are automatic for simple CRUD with no need to manually control the CRUD