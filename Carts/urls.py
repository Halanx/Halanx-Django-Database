from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart_list),
    url(r'^(?P<pk>[0-9]+)/active', views.cart_itemlist_active),
    url(r'^(?P<no>[0-9]+)/', views.cart_id),     # fetch cart according to phone number
    url(r'^items/$', views.item_list),
    url(r'^items/(?P<pk>[0-9]+)', views.item_id),
    url(r'^itemlist/(?P<pk>[0-9]+)', views.cart_itemlist),
]

