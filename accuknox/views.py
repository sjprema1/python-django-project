from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Person
from .forms import CreateNewPersons
from .forms import UploadFileForm

# Create your views here.

def base(response,id):
    x = Person.objects.get(id=id)
    return render(response,"base.html",{'x':x})

def home_page(response):
    x = Person.objects.all()
    return render(response,"home.html",{"person":x})

def create(response):
    if response.method=="POST":
        form = CreateNewPersons(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = form.cleaned_data["age"]
            d="5678-09-09"
            t = Person(name=n,age =a,dob=d)
            t.save()
            return HttpResponseRedirect("/%i" %t.id)
    form = CreateNewPersons()

    return render(response,"create.html",{"form":form})

def upload_file(response):
    upload_forms =UploadFileForm()
    return render(response,"upload.html",{'form':upload_forms})
