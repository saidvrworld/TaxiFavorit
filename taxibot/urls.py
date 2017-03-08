from django.conf.urls import url
from taxibot import views


urlpatterns = [url(r'^$', views.CallListView.as_view(), name='callList'),
               url(r'^$', views.NeedCarList.as_view(), name='needCarList'),
               url(r'^setDriver/$',views.setDriver, name='setDriver'),
               url(r'^SendDriver/$', views.SendDriver, name='sendDriver'),
               url(r'^clearDB/$', views.clearDB, name='clearDB'),
               url(r'^clearDBHistory/$', views.clearDBHistory, name='clear_db_history'),

               url(r'^callsWithCar/$', views.calls_with_car_ListView.as_view(), name='calls_with_car'),
               url(r'^accepted/$', views.acceptedCalls.as_view(), name='accepted'),
               url(r'^setArrived/$', views.EndCall, name='send_arrived'),

               url(r'^DBList/$', views.DBCalls.as_view(), name='db_list'),

               url(r'^webhook/$', views.webhook, name='webhook'),
               url(r'^309803225:AAEfkOtjUfLCTSHicJD05uy7AvilTCkzOYs/$', views.getUpdate, name='get_update'),

               ]
