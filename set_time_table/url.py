from django.conf.urls import url
from set_time_table import views
urlpatterns=[
    url('^set-t-table',views.set_table),
]