from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from upload_study_material.models import UploadStudyMaterial
# Create your views here.
def upload(request):
    if request.method == "POST":
        obj = UploadStudyMaterial()
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.material = myfile.name
        obj.semester = request.POST.get("semester")
        obj.teacher_id = request.session["uid"]
        obj.save()
    return render(request,'upload_study_material/upload_study_material.html')
