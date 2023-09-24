from django.contrib import admin
from .models import Booking, Department,Doctors
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Booking)