from django.shortcuts import render
from register_dep.models import RegisterDep
# Create your views here.
def registerdep(request):
    if request.method == "POST":
        obj = RegisterDep()
        obj.name = request.POST.get("name")
        obj.info = request.POST.get("info")
        obj.save()
    return render(request,'register_dep/post_dep_info.html')