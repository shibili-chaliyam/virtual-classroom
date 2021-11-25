from django.conf.urls import url
from upload_study_material import views
urlpatterns=[
    url('^upload',views.upload),
]