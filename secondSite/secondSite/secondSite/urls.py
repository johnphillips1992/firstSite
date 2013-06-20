from django.conf.urls import patterns, include, url
from books.views import PublisherList, PublisherView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^form/$', PublisherView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    )
