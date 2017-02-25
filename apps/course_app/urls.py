from django.conf.urls import url

from . import views

urlpatterns = [
	# Need to add id to process/destroy route
	url(r'^process/destroy/(?P<id>\d+)/delete$', views.delete),
	url(r'^process/destroy/(?P<id>\d+)$', views.destroy),
	url(r'^process$', views.process),
	url(r'^$', views.index),
]
 
