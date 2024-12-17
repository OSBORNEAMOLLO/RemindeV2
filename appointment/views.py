from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import AppointmentForm, ConsultationForm, UserForm
from .models import Appointment, Consultation, UserProfile

IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png']  # Ensure this is defined


def create_appointment(request):
    if not request.user.is_authenticated:
        return redirect('appointment:login_user')
    
    form = AppointmentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.user = request.user
        appointment.doctor = request.user
        
        file_type = appointment.image.name.split('.')[-1].lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {'appointment': appointment, 'form': form, 'error_message': 'Invalid file type.'}
            return render(request, 'appointment/create_appointment.html', context)
        
        appointment.save()
        return redirect('detail', appointment_id=appointment.id)
    
    return render(request, 'appointment/create_appointment.html', {'form': form})


def create_consultation(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    form = ConsultationForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        if appointment.consultation_set.filter(doctor=form.cleaned_data['doctor']).exists():
            context = {'appointment': appointment, 'form': form, 'error_message': 'Consultation already exists.'}
            return render(request, 'appointment/create_consultation.html', context)
        
        consultation = form.save(commit=False)
        consultation.appointment = appointment
        consultation.save()
        return redirect('detail', appointment_id=appointment.id)
    
    return render(request, 'appointment/create_consultation.html', {'appointment': appointment, 'form': form})


def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, user=request.user)
    appointment.delete()
    return redirect('index')


def delete_consultation(request, appointment_id, consultation_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    consultation.delete()
    return redirect('detail', appointment_id=appointment.id)


def detail(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect('appointment:login_user')
    
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointment/detail.html', {'appointment': appointment})


def isdoctor(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    consultation.is_doctor = not consultation.is_doctor
    consultation.save()
    return JsonResponse({'success': True})


def favorite_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.is_doctor = not appointment.is_doctor
    appointment.save()
    return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'appointment/index.html')
    
    appointments = Appointment.objects.filter(user=request.user)
    query = request.GET.get('q')
    
    if query:
        appointments = appointments.filter(
            Q(doctor__icontains=query) |
            Q(patient_name__icontains=query)
        ).distinct()
        consultation_results = consultation_results.filter(
            Q(doctor__icontains=query)
        ).distinct()
        return render(request, 'appointment/index.html', {
            'appointments': appointments,
            'consultations': consultation_results,
        })
    
    return render(request, 'appointment/index.html', {'appointments': appointments})


def logout_user(request):
    logout(request)
    return render(request, 'appointment/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('appointment:index')
        return render(request, 'appointment/login.html', {'error_message': 'Invalid login'})
    
    return render(request, 'appointment/login.html')

from django.shortcuts import render

def dashboard(request):
    return render(request, 'appointment/dashboard.html')

def home(request):

    context = {
        'title': 'Health Tracker'
    }
    return render(request, 'health/home.html', context)



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        

        phone_number = form.cleaned_data.get('phone_number')
        address = form.cleaned_data.get('address')
        UserProfile.objects.create(user=user, phone_number=phone_number, address=address)
        user.save()
        login(request, user)
        return redirect('appointment:index')
    
    return render(request, 'appointment/register.html', {'form': form})


def consultations(request, filter_by):
    if not request.user.is_authenticated:
        return redirect('appointment:login_user')
    
    consultations = Consultation.objects.filter(appointment__user=request.user)
    if filter_by == 'doctor':
        consultations = consultations.filter(is_favorite=True)
    
    return render(request, 'appointment/consultations.html', {
        'consultation_list': consultations,
        'filter_by': filter_by,
    })
