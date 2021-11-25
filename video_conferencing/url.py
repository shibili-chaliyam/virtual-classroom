from django.conf.urls import url
from video_conferencing import views
urlpatterns=[
    url('^upload',views.upload_conf),
]