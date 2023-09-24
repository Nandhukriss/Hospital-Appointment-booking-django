from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={

            "booking_date":DateInput(),
            'p_name': forms.TextInput(attrs={'placeholder': 'Patient Name'}),
            'p_phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'p_email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'doc_name': forms.Select(attrs={'placeholder': 'Select Doctor'}),
           
        }

# Override the label for the doc_name field
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['doc_name'].empty_label = 'Select Doctor'

        # Remove labels for specific fields
        self.fields['p_name'].label = False
        self.fields['p_phone'].label = False
        self.fields['p_email'].label = False
        self.fields['doc_name'].label = False
        self.fields['booking_date'].label = False