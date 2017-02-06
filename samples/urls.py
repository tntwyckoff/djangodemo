from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bmi_imp/(?P<weight>\w+)/(?P<height>\w+)/$', views.bmi_imperial, name='bmi_imperial'),
    url(r'^bmi/(?P<weight>\w+)/(?P<height>\w+)/$', views.bmi_metric, name='bmi_metric'),
]