from django.shortcuts import render
from internal_time_table.models import InternalTimeTable

# Create your views here.
def internal_time_table(request):
    if request.method == "POST":
        obj = InternalTimeTable()
        obj.date = request.POST.get("exam_date")
        obj.subject = request.POST.get("exam_sub")
        obj.start_time = request.POST.get("exam_time")
        obj.ending_time = request.POST.get("exam_time2")
        obj.save()
    return render(request,'internal_time_table/post_int_exam.html')
