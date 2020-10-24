from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def crsipy_form(request):
    form=Crispyform()
    if request.method=="POST":
        form_data=Crispyform(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'crispy.html',context={'form':form})