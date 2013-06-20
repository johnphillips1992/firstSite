from django.conf.urls.defaults import patterns, url
from polls import views

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
        url(r'^polls/', include('polls.urls', namespace="polls")),
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
        )
