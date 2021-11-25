from django.shortcuts import render
from set_time_table.models import SetTimeTable
# Create your views here.
def set_table(request):
    if request.method == "POST":
        obj = SetTimeTable()
        obj.day = request.POST.get("day")
        obj.subject = request.POST.get("subject")
        obj.period = request.POST.get("period")
        obj.teacher_name = request.POST.get("teacher_name")
        obj.save()
    return render(request,'set_time_table/set_time_table.html')