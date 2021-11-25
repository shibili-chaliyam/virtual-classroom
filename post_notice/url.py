from django.conf.urls import url
from post_notice import views
urlpatterns=[
    url('^notice',views.post_notice),

]