from django.conf.urls import patterns, include, url

from django.contrib import admin
from accounts.forms import SignupFormExtra
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pfe_v1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','userena.views.signup',{'signup_form': SignupFormExtra}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'^verif/', include('sms_verif.urls')),
)
