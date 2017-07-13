from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Products import views


urlpatterns = [
    url(r'^$', views.product_list),
    url(r'^(?P<pk>[0-9]+)/upload-image', views.upload_photo),
    url(r'^(?P<pk>[0-9]+)', views.product_id),

]









