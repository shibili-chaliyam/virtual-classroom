from django.conf.urls import url
from register_dep import views
urlpatterns=[
    url('^dep_info',views.registerdep),
]