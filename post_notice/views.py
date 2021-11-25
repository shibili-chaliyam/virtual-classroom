from django.shortcuts import render
from post_notice.models import PostNotice
# Create your views here.
def post_notice(request):
    if request.method == "POST":
        obj = PostNotice()
        obj.content = request.POST.get("content")
        obj.date = request.POST.get("date")
        obj.save()
    return render(request,'post_notice/post_notice.html')