from django.conf.urls import url
from django.contrib import admin
from .views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostCreateAPIView


urlpatterns = [
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^$', PostListAPIView.as_view(), ),
    url(r'^(?P<slug>\w+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>\w+)/edit/$', PostUpdateAPIView.as_view(), name='update'),

]