from django.conf.urls import url
from .views import (Homeview, Orderview, Helpview, Loginview, Logoutview,
                    Customview, Menuview, Registerview, AddToCartview, Orderhistory)

urlpatterns = [
    url(r'^$', Homeview.as_view(), name='Home'),
    url(r'^login$', Loginview.as_view(), name='Login'),
    url(r'^logout$', Logoutview.as_view(), name='Logout'),
    url(r'^help$', Helpview.as_view(), name='Help'),
    url(r'^custom$', Customview.as_view(), name='Custom'),
    url(r'^register$', Registerview.as_view(), name='Register'),
    url(r'^menu/(?P<menu_type>.+)/$', Menuview.as_view(), name='Menu'),
    url(r'^order/$', Orderview.as_view(), name='Order'),
    url(r'^orederhistory', Orderhistory.as_view(), name='Orderhistory'),
    url(r'^ajax_process$', AddToCartview.as_view(), name='AddToCart'),
  ]

