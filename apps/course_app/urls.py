from django.conf.urls import url

from . import views

urlpatterns = [
	# Need to add id to process/destroy route
	url(r'^process/destroy/(?P<id>\d+)/delete$', views.delete, name='courses_delete'),
	url(r'^process/destroy/(?P<id>\d+)$', views.destroy, name='courses_destroy'),
	url(r'^process$', views.process, name='courses_process'),
	url(r'^$', views.index, name='courses_index'),
]
