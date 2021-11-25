from django.conf.urls import url
from login import views
urlpatterns=[
    url('^login/',views.login),
    url('^login1/',views.stu_login),
]