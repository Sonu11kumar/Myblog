from django.conf.urls import url
from .import views
from .views import JoinFormView
app_name = 'blogapp'

urlpatterns = [
    url(r'^create/$', views.post_create, name="post_create"),
    url(r'^list/$', views.list, name="list"),
    url(r'^details/(?P<id>\d+)/$', views.details, name="details"),
    url(r'^join/', JoinFormView.as_view()),

]