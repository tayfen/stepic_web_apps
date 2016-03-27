from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import *

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r"^$", top),
    url(r"^login/.*$", login_user),
    url(r"^signup/.*$", signup),
    url(r"^ask/.*$", ask),
    url(r"^answer/.*$", answer),
    url(r"^popular/.*$", pop),
    url(r"^new/.*$", test),
    url(r"^question/(\d+)/$", question),
    # url(r"^blog/", include("blog.urls")),
    # url(r"^admin/", include(admin.site.urls)),
]

