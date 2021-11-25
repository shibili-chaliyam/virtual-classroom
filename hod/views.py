from django.shortcuts import render
from hod.models import Hod
from login.models import Login
from register_dep.models import RegisterDep


# Create your views here.
def managehod(request):
    obj = Hod.objects.all()
    context = {
        'objval': obj,
    }
    return render(request, 'hod/manage_hod.html', context)


def hodreg(request):
    ob = RegisterDep.objects.all()
    context = {
        'val': ob,
    }
    if request.method == "POST":
        obj = Hod()
        obj.name = request.POST.get("hod_name")
        obj.address = request.POST.get("hod_address")
        obj.qualification = request.POST.get("hod_qual")
        obj.dep_id = request.POST.get("dep_id")
        obj.mobile = request.POST.get("mobile")
        obj.save()

        ob = Login()

        ob.username = obj.name
        ob.password = request.POST.get("passw")
        ob.uid = obj.id
        ob.type = "hod"
        ob.save()
    return render(request, 'hod/hod_reg.html',context)


# def approve(request,idd):
#     obj=Hod.objects.get(id=idd)
#     obj.status="approved"
#     obj.save()
#     return managehod(request)


# def reject(request,idd):
#     obj=Hod.objects.get(id=idd)
#     obj.status="reject"
#     obj.save()
#     return managehod(request)


def edit(request,idh):

    obj = Hod.objects.filter(id=idh)
    context = {
        'objval': obj,
    }
    if request.method == "POST":
        ob = Hod.objects.get(id=idh)
        ob.name = request.POST.get("hod_name")
        ob.qualification = request.POST.get("hod_qual")
        ob.mobile = request.POST.get("mobile")
        ob.department = request.POST.get("hod_dep")
        ob.address = request.POST.get("hod_address")
        ob.save()
        return managehod(request)
    return render(request,'hod/edit_hod.html', context)


def delete(request,ich):
    obj = Hod.objects.get(id=ich)
    obj.delete()

    return managehod(request)