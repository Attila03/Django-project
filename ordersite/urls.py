from django.conf.urls import url
from .views import (Homeview, Pizzaorderview, Helpview, Loginview, Logoutview,
                    Customview, Menuview, Registerview)

urlpatterns = [
    url(r'^$', Homeview.as_view(), name='home'),
    url(r'^Login$', Loginview.as_view(), name='Login'),
    url(r'^Logout$', Logoutview.as_view(), name='Logout'),
    url(r'^Help$', Helpview.as_view(), name='Help'),
    url(r'^Custom$', Customview.as_view(), name='Custom'),
    url(r'^Register$', Registerview.as_view(), name='Register'),
    url(r'^Menu/(?P<menu_type>.+)/$', Menuview.as_view(), name='Menu'),
    url(r'^(?P<pizza_name>.+)/$', Pizzaorderview.as_view(), name='Pizzaorder'),
  ]

