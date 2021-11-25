from django.conf.urls import url
from hod import views
urlpatterns=[
    url('^hodreg/',views.hodreg),
    url('^manage',views.managehod,name='manage'),
    url('^edit/(?P<idh>\w+)', views.edit, name="edit"),
    url('^delete/(?P<ich>\w+)', views.delete, name="delete"),

]