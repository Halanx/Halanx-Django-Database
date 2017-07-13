from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.order_list),                      # returns all orders, post here
    url(r'^(?P<pk>[0-9]+)/items', views.order_items),  # return items of a specific order
    url(r'^(?P<pk>[0-9]+)', views.order_id),           # return a specific order
    url(r'^user/(?P<pk>[0-9]+)', views.user_orders),   # return all orders of a user
]









