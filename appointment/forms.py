from django.contrib.auth.models import User
from django import forms

from .models import Appointment, Consultation, UserProfile


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Select a date'})
    )


    class Meta:
        model = Appointment
        fields = ['date', 'patient_name', 'doctor', 'time', 'file_number', 'is_doctor']


class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation
        fields = ['consultation_number', 'doctor_name','patient_name', 'file_number', 'is_doctor']

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email','Phone Number', 'password', "Confirm Password", ]

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    phone_number = forms.CharField(max_length=15, label="Phone Number")  # New field
    address = forms.CharField(widget=forms.Textarea, label="Address")    # New field

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'confirm_password', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
