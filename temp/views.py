from django.shortcuts import render

# Create your views here.
def hod(request):
    return render(request, 'temp/hod.HTML')
def admin(request):
    return render(request, 'temp/admin.html')

def tea(request):
    return render(request,'temp/teachers.html')