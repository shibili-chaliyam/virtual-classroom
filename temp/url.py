from django.conf.urls import url
from temp import views
urlpatterns=[
    url('^hod',views.hod),
    url('^tea',views.tea),
    url('^admin',views.admin,name='admin'),
]