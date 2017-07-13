from django.conf.urls import url
from ShopperBase import views


urlpatterns = [
    url(r'^$', views.shopper_list),
    url(r'^(?P<no>[0-9]+)/$', views.shopper_id),
    url(r'^(?P<pk>[0-9]+)/upload-image', views.upload_image),
    url(r'^documents/$', views.post_documents),
    url(r'^documents/(?P<who>[0-9]+)/$', views.get_documents),
]









