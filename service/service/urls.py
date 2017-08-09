from django.conf.urls import url, include
from rest_framework import routers
from service.collect import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^devdiff/v0/result/$', views.result),
    url(r'^devdiff/v0/results/$', views.results),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
