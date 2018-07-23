from django.conf.urls import url, include
from cauth.views import DemoUserView, DemoUserListView, DemoAPIView, DemoGListAPIView, DemoGRetrieveAPIView, DemoListAPIView
from rest_framework import routers
from .views import UserViewSet, LoginView, loginout, getuser
router_user = routers.DefaultRouter(trailing_slash=False)
router_user.register('', UserViewSet)

urlpatterns = [
    url(r'^', include(router_user.urls)),
    url(r'^loginout$', loginout),
    url(r'^login$', LoginView.as_view()),
    # --------------------demo---------------------------
    url(r'^getuser/', getuser),
    url(r'^demouserlist/', DemoUserListView.as_view()),
    url(r'^demouser/', DemoUserView.as_view()),
    url(r'^demouserapiview/', DemoAPIView.as_view()),
    url(r'^demousergrapi/(?P<pk>[0-9]+)/', DemoGRetrieveAPIView.as_view()),
    url(r'^demouserglapi/', DemoGListAPIView.as_view()),
    url(r'^demouserlapi/', DemoListAPIView.as_view()),
]
