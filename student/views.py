from django.shortcuts import render
from student.models import Student
from register_dep.models import RegisterDep
from upload_study_material.models import UploadStudyMaterial
from  video_conferencing.models import VideoConferencing
from  post_notice.models import PostNotice
from set_time_table.models import SetTimeTable
from internal_time_table.models import InternalTimeTable
from login.models import Login

# Create your views here.
def view_dep(request):
    obj = RegisterDep.objects.all()
    contest={
        'objval': obj,
    }
    return render(request,"student/view_dep_info.html",contest)

def down_material(request):
    obj=UploadStudyMaterial.objects.all()
    contest={
        'objval' :obj,
    }
    return render(request,"student/Down_s_material.html",contest)

def join_meet(request):
    obj=VideoConferencing.objects.all()
    contest={
        'objval':obj,
    }
    return render(request,"student/join_meet.html",contest)


def student_reg(request):
    if request.method =="POST":
        obj = Student()
        obj.name = request.POST.get("name")
        obj.address = request.POST.get("address")
        obj.semester = request.POST.get("semester")
        obj.contact = request.POST.get("mobile")
        obj.course = request.POST.get("course")
        obj.save()

        ob=Login()
        ob.username=request.POST.get("name")
        ob.password = request.POST.get("pass")
        ob.type = "student"
        ob.uid = obj.id
        ob.save()
    return render(request,'student/register.html')


def view_notice(request):
    obj = PostNotice.objects.all()
    contest = {
        'objval':obj,
    }
    return render(request,"student/view_notice.html",contest)

def view_xtable(request):
    obj = InternalTimeTable.objects.all()
    contest = {
        'objval' : obj,
    }
    return render(request,"student/view_exam_table.html",contest)

def view_timetable(request):
    obj = SetTimeTable.objects.all()
    context = {
        'objval' : obj,
    }
    return render(request,"student/view_timetable.html",context)


def manage_std(request):
    obj = Student.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,"student/manage_student.html",context)


def approve(request,idd):
    obj=Student.objects.get(id=idd)
    obj.status="approved"
    obj.save()
    return manage_std(request)


def reject(request,idd):
    obj=Student.objects.get(id=idd)
    obj.status="reject"
    obj.save()
    return manage_std(request)