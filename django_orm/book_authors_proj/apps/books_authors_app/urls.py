from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<id>\d+)$', views.authDetails),
    url(r'^books/(?P<id>\d+)$', views.bookDetails),

]