from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^process_money$', views.check),
    url(r'^restart$', views.restart),
]