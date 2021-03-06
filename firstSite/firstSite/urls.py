from django.conf.urls import patterns, include, url
from polls import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^polls/', include('firstSite.urls', namespace="polls")),
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
        url(r'^admin/', include(admin.site.urls)),
        )
