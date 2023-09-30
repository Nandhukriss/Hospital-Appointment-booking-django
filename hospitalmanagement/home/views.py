from django.shortcuts import render
from .models import Department,Doctors
from .forms import BookingForm
from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
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
            sender_email = request.POST.get('p_email')
            sender_name = request.POST.get('p_name')
            doc_id = request.POST.get('doc_name')  # Get the doctor's ID from the form
            doctor = Doctors.objects.get(pk=doc_id)  # Query the Doctors model to get the doctor's name
            doc_name = doctor.doc_name 
            form.save()
            msg = "Your Apointment Has been Confirmed"

            # Your email content template (as shown above)
            email_template = 'email_message.html'
            # Replace placeholders with actual values
            email_body = render_to_string(email_template, {'patient_name': sender_name, 'doctor_name': doc_name})

            subject = 'APPOINTMENT'  # Email subject
            from_email = 'nandhu.r.s.krishna@gmail.com'  # Sender's email address
            recipient_list = [sender_email]  # List of recipient email addresses
            
            # message = f'HEY {sender_name} This is From City Hospital Your Apointment with {doc_name} Has been Confirmed'  # Email message
            # send_mail(subject, message, from_email, recipient_list)//without html

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'  # Set the content type to HTML
            email.send()

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