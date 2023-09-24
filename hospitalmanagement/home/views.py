from django.shortcuts import render
from .models import Department,Doctors
from .forms import BookingForm
# Create your views here.

def index(request):
    return render (request,'index.html')

def about(request):
   return render (request,'about.html')

def booking(request):
    msg = None

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Your Apointment Has been Confirmed"
            return render(request, 'booking.html', {'form': form, 'msg': msg})
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form, 'msg': msg})

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