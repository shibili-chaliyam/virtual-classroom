from django.conf.urls import url
from internal_time_table import views
urlpatterns=[
    url('^internal_table/',views.internal_time_table),
]