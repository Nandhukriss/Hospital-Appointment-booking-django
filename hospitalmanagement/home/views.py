from django.shortcuts import render
from .models import Department,Doctors
from .forms import BookingForm
# Create your views here.

def index(request):
    return render (request,'index.html')

def about(request):
   return render (request,'about.html')

def booking(request):
    form=BookingForm()
    dic_form={
        'form':form
    }
    return render (request,'booking.html',dic_form)

def doctors(request):
    doc_dict={
        "doc":Doctors.objects.all()
    }
    return render (request,'doctors.html',doc_dict)

def contact(request):
    return render (request,'contact.html')

def department(request):

    dep_dict={
        "dep":Department.objects.all()
    }
    return render (request,'department.html',dep_dict)