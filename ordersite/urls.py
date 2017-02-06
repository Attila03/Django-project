from django.conf.urls import url
from .views import Homeview, Vegview, Nonvegview, Allview, Pizzaorderview, Helpview, Customview

urlpatterns = [
    url(r'^$', Homeview.as_view(), name='home'),
    url(r'^All$', Allview.as_view(), name='All'),
    url(r'^Veg$', Vegview.as_view(), name='Veg'),
    url(r'^Nonveg$', Nonvegview.as_view(), name='Nonveg'),
    url(r'^(?P<pizza_name>.+)/$', Pizzaorderview.as_view(), name='Pizzaorder'),
    url(r'^Help$', Helpview.as_view(), name='Help'),
    url(r'^Custom$', Customview.as_view(), name='Custom')
]

