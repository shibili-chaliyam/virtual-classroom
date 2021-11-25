from django.shortcuts import render
from teacher.models import Teacher
from login.models import Login
from register_dep.models import RegisterDep
# Create your views here.
def manageteacher(request):
    obj = Teacher.objects.all()
    context = {
        'objval': obj,
    }
    return render(request,'teacher/manage_teacher.html',context)


def register(request):
    ob=RegisterDep.objects.all()
    context={
        'val':ob,
    }
    if request.method == "POST":
        obj = Teacher()
        obj.name = request.POST.get("name")
        obj.subject = request.POST.get("subject")
        obj.qualification = request.POST.get("qualification")
        obj.mob_no = request.POST.get("mob_no")
        obj.dep_name = request.POST.get("dept")

        obj.save()
        ob=Login()
        ob.username=request.POST.get("name")
        ob.password=request.POST.get("pass")
        ob.type = "teacher"
        ob.uid = obj.id
        ob.save()
    return render(request,'teacher/register_teacher.html',context)


def edit(request,idd):
    obj = Teacher.objects.filter(id=idd)
    context = {
        'objval': obj,
    }
    if request.method == "POST":
        obj = Teacher.objects.get(id=idd)
        obj.name = request.POST.get("name")
        obj.subject = request.POST.get("subject")
        obj.qualification = request.POST.get("qualification")
        obj.mob_no = request.POST.get("mob_no")
        obj.dep_name = request.POST.get("dep_name")
        obj.address = request.POST.get("address")
        obj.save()
        return manageteacher(request)
    return render(request,'teacher/edit_teacher.html',context)


def delete(request,icc):
    obj = Teacher.objects.get(id=icc)
    obj.delete()

    return manageteacher(request)

