from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xiaojuren.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^index$', 'xiaojuren.views.home'),
	url(r'^upload$', 'xiaojuren.views.upload'),
	url(r'^null$', 'xiaojuren.views.null'),	
	url(r'^text$', 'xiaojuren.views.text'),
	url(r'^add$', 'xiaojuren.views.add'),

	url(r'^all_left$', 'xiaojuren.views.all_left'),
	
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
)
