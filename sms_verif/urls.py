from django.conf.urls import patterns, url

urlpatterns = patterns('sms_verif.views',
    url(r'^code/$', 'code'),
)
