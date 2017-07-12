from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.batch_list),
    url(r'^(?P<pk>[0-9]+)', views.batch_id),
    url(r'^(?P<pk>[0-9]+)/orders', views.batch_id_orders),      # function to get all orders having this batch number
    url(r'^(?P<no>[0-9]+)/batches', views.shopper_batches),
]




