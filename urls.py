from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('textshare.views',
    # Examples:
    # url(r'^$', 'writeboard.views.home', name='home'),
    # url(r'^writeboard/', include('writeboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'index'),
    url(r'^(?P<note_key>\d+)/$', 'show_note'),
    url(r'^save/$', 'save_note'),
    
    url(r'^admin/', include(admin.site.urls))
)
