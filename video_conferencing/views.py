from django.shortcuts import render
from video_conferencing.models import VideoConferencing
# Create your views here.
def upload_conf(request):
    if request.method == "POST":
        obj = VideoConferencing()
        obj.link = request.POST.get("meet_link")
        obj.semester = request.POST.get("semester")
        obj.save()
    return render(request,'video_conferencing/upload_conf_link.html')