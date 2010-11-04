from django.conf.urls.defaults import *

urlpatterns = patterns('browserinfo.views',
        url(regex=r'^$',
            view='detect_info',
            name='browserinfo'
            ),
)


