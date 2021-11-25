from django.conf.urls import url
from student import views

urlpatterns=[
    url('^view_dep',views.view_dep),
    url('^down_material',views.down_material),
    url('^meet',views.join_meet),
    url('^notice',views.view_notice),
    url('^exam_table',views.view_xtable),
    url('^time_table',views.view_timetable),
    url('^reg_std',views.student_reg),
    url('^manage',views.manage_std),
    url('^approve/(?P<idd>\w+)', views.approve, name="approve"),
    url('^reject/(?P<idd>\w+)', views.reject, name="reject"),
]