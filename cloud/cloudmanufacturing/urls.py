from django.conf.urls import patterns, url

from cloudmanufacturing import views

urlpatterns = patterns('',
	url(r'^$', views.index),
)