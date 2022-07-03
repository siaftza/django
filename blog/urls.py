## importing django's function path and all views fom blog app

from django.urls import path
from . import views

urlpatterns = [
    ## assigns view called post_list to ROOT url. Basically, post list is
    ## correct place to send someone visiting via address
    ## post_list is the name of the url used to identify the view
    ## important to name each url in the app!
    path('', views.post_list, name='post_list'),
]