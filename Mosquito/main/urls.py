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
    url('data/', views.data.as_view(), name='data'),
]