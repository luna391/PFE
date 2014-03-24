from django.conf.urls import patterns, include, url
from forms import SignupFormExtra

urlpatterns = patterns('',
url(r'^signup/$',
    'userena.views.signup',
    {'signup_form': SignupFormExtra}),
)
