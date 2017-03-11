from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<account_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^addaccount$', views.add_account, name='add_account'),
    url(r'^delaccount$', views.del_account, name='del_account'),
    url(r'^editname/(?P<account_id>[0-9]+)$',views.editname,name='editname'),
]