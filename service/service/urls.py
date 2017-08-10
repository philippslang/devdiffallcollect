from django.conf.urls import url, include
from rest_framework import routers
from service.collect import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^devdiff/v0/result/$', views.result),
    url(r'^devdiff/latest/result/$', views.result),
    url(r'^devdiff/v0/results/$', views.results_v0),
    url(r'^devdiff/latest/results/$',  views.ResultsView.as_view({'get': 'list'})),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
