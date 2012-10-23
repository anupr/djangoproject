from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('djangoproject.web.views',

	url(r'^$','index',name='index'),
	url(r'^fblogin$','fblogin', name='fblogin'),
)