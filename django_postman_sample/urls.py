from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^messages/", include("postman.urls", namespace="postman")),
    url(r'^$', TemplateView.as_view(template_name="site_base.html"), name="home")
)
