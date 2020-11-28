from django.conf.urls import url

from .views import exchange_token

urlpatterns = [
    url(r'social/(?P<backend>[^/]+)/$', exchange_token)
]
