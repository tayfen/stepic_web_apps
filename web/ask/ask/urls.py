from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r"^$", test),
    url(r"^login/.*$", top),
    url(r"^signup/.*$", test),
    url(r"^ask/.*$", test),
    url(r"^popular/.*$", pop),
    url(r"^new/.*$", test),
    url(r"^question/(\d+)/$", question),
    # url(r"^blog/", include("blog.urls")),
    # url(r"^admin/", include(admin.site.urls)),
]

