from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.item_list),
    url(r'^(?P<pk>[0-9]+)', views.items_id),

]





