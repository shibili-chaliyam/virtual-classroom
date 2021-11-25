from django.conf.urls import url
from teacher import views
urlpatterns=[
    url('^manage',views.manageteacher),
    url('^register',views.register),
    url('^edit/(?P<idd>\w+)', views.edit, name="edit"),
    url('^delete/(?P<icc>\w+)', views.delete, name="delete"),
]
