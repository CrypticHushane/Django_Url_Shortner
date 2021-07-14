from django.shortcuts import redirect, render
from django.http import HttpResponse
import uuid
from .models import Url
# Create your views here.
def home(request):
    return render(request,'shortner/index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = url,uid = uid)
        new_url.save()
        return HttpResponse(uid)

def detail(request, id):
    url = Url.objects.get(uid=id)
    return redirect(url.link)
    
