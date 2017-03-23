from django.conf.urls import url
from .views import (Homeview, Orderview, Helpview, Loginview, Logoutview,
                    Customview, Menuview, Registerview, AddToCartview)

urlpatterns = [
    url(r'^$', Homeview.as_view(), name='Home'),
    url(r'^Login$', Loginview.as_view(), name='Login'),
    url(r'^Logout$', Logoutview.as_view(), name='Logout'),
    url(r'^Help$', Helpview.as_view(), name='Help'),
    url(r'^Custom$', Customview.as_view(), name='Custom'),
    url(r'^Register$', Registerview.as_view(), name='Register'),
    url(r'^Menu/(?P<menu_type>.+)/$', Menuview.as_view(), name='Menu'),
    url(r'^Order/$', Orderview.as_view(), name='Order'),
    url(r'^ajax_process$', AddToCartview.as_view(), name='AddToCart'),
  ]

