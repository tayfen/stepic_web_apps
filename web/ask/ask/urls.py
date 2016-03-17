from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("qa.views",
    # Examples:
    url(r"^$", "test"),
    url(r"^login/.*$", "test"),
    url(r"^signup/.*$", "test"),
    url(r"^ask/.*$", "test"),
    url(r"^popular/.*$", "test"),
    url(r"^new/.*$", "test"),
    url(r"^question/(\d+)/$", "test"),
    # url(r"^blog/", include("blog.urls")),
    # url(r"^admin/", include(admin.site.urls)),
)

