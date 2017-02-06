from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<phone>\w+)/(?P<message>\w+)/$', views.handlePost, name='Post an SMS'),
]