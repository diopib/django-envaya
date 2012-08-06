from django.conf.urls.defaults import patterns, include, url
from envaya import views

urlpatterns = patterns('',
	url(r'^/', 'envaya.views.home'),
	url(r'^admin/', 'envaya.views.admin'),
)