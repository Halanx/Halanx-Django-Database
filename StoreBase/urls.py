from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from StoreBase import views


urlpatterns = [
    url(r'^$', views.store_list),
    url(r'^(?P<pk>[0-9]+)/upload-logo', views.upload_logo),
    url(r'^(?P<pk>[0-9]+)$', views.store_id),
    url(r'^(?P<store>[0-9]+)/products$', views.store_products),
]



