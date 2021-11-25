from django.shortcuts import render
from login.models import Login

from login.models import Login
# Create your views here.
def login(request):
    if request.method=="POST":
        uname=request.POST.get('user')
        psw=request.POST.get('pass')
        obj = Login.objects.filter(username=uname,password=psw)
        # if obj:
        tp =""
        for ob in obj:
            tp =ob.type
            uiid = ob.login_id
            if tp=="admin":
                request.session['uid'] = uiid
                return render(request,'temp/admin.html')
            elif tp=="hod":
                request.session['uid'] = uiid
                return render(request, 'temp/hod.html')
            elif tp=="teacher":
                request.session['uid'] = uiid
                return render(request, 'temp/teachers.html')
            # else:
        objlist="invalid credentials"
        context={
                'obj':objlist,
        }
        return render(request,'login/admin_login.html',context)
                # return render(request,'login/admin_login.html')
    return render(request,'login/admin_login.html')



def stu_login(request):
    if request.method=="POST":
        uname=request.POST.get('user')
        psw=request.POST.get('pass')
        obj = Login.objects.filter(username=uname,password=psw)
        tp =""
        for ob in obj:
            tp =ob.type
            uiid = ob.login_id
            if tp=="student":
                request.session['uid'] = uiid
                return render(request,'temp/student.html')
        objlist="invalid credentials"
        context={
                'obj':objlist,
        }
        return render(request, 'login/student_login.html', context)
    return render(request, 'login/student_login.html')