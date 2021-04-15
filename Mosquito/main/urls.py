from django.urls import path
from main import views
from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.main, name='main'),
    path("map/", views.maps, name="map"),
    path("base/", views.base, name="base"),
    path("search/", views.search, name="search"),
    url("bar/", views.ChartView.as_view(), name='bar'),
    url('bar2/', views.ChartView2.as_view(), name='bar2'),
    url('bar3/', views.ChartView3.as_view(), name='bar3'),
    url('bar4/', views.ChartView4.as_view(), name='bar4'),
    url('bar5/', views.ChartView5.as_view(), name='bar5'),
    url('bar6/', views.ChartView6.as_view(), name='bar6'),
    url('bar7/', views.ChartView7.as_view(), name='bar7'),
    url('bar8/', views.ChartView8.as_view(), name='bar8'),
    url('bar9/', views.ChartView9.as_view(), name='bar9'),
    url('bar10/', views.ChartView10.as_view(), name='bar10'),
    url('bar11/', views.ChartView11.as_view(), name='bar11'),
    url('bar12/', views.ChartView12.as_view(), name='bar12'),
    url('data/', views.data.as_view(), name='data'),
    url('data2/', views.data2.as_view(), name='data2'),
    url('data3/', views.data3.as_view(), name='data3'),
]