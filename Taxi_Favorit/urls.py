from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [url(r'^taxibot/',include('taxibot.urls',namespace='taxibot')),
    url(r'^admin/', admin.site.urls),
               ]

