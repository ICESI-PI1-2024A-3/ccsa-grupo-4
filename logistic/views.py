from django.shortcuts import render
from django.http import HttpResponse
# In here, we must create the HTMLs
# Create your views here.

def home(request):
    return HttpResponse("Home page")

def event_checklist(request):
    
    return render(request, "event_checklist.html")
    

