from django.conf.urls import url

from . import views

app_name = 'show_gallery'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^check_user/$', views.Check_UserView.as_view(), name='check_user'),
    url(r'^(?P<pk>[0-9]+)/template1/$', views.Template1View.as_view(), name='template1'),
    url(r'^(?P<pk>[0-9]+)/template2/$', views.Template2View.as_view(), name='template2'),
    url(r'^(?P<pk>[0-9]+)/template3/$', views.Template3View.as_view(), name='template3'),
    url(r'^(?P<pk>[0-9]+)/template4/$', views.Template4View.as_view(), name='template4'),
    url(r'^(?P<pk>[0-9]+)/template5/$', views.Template5View.as_view(), name='template5'),
]