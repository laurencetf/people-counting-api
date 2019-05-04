"""
Definition of urls for People-counting.
"""

from datetime import datetime
import site
from . import settings
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^register/', include('Register.urls'), name='register'),
    url(r'^authenticate/', include('Authenticate.urls'), name='authenticate'),
    url(r'^verify-authentication/', include('VerifyAuthentication.urls'), name='verifyAuthentication'),
    url(r'^project/', include('Project.urls'),name="project"),
    url(r'^clicks/', include('Clicks.urls'),name="clicks"),
    url(r'^test/', include('Test.urls'),name="test"),
    url(r'^admin/', include(admin.site.urls))
]