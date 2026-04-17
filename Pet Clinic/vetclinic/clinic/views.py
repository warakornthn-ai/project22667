from django.shortcuts import render, redirect  
from .models import Pet
from .forms import PetForm  
from django.db.models import Q

from django.db.models import Q

def home(request):
    query = request.GET.get('q')

    records = []

    if query:
        records = MedicalRecord.objects.filter(
            Q(pet__name__icontains=query) |
            Q(pet__species__icontains=query) |
            Q(pet__owner__name__icontains=query) |
            Q(pet__owner__owner_id__icontains=query)
        )

    return render(request, 'home.html', {
        'query': query,
        'records': records
    })

from .forms import AppointmentForm

from django.shortcuts import render, redirect
from .forms import AppointmentForm

def book(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointments')  # 🔥 สำคัญมาก

    else:
        form = AppointmentForm()

    return render(request, 'book.html', {'form': form})

from django.utils.timezone import now
from .models import Appointment

from datetime import date

def dashboard(request):
    today = date.today()
    appointments = Appointment.objects.filter(appointment_date__date=today)

    return render(request, 'dashboard.html', {
        'appointments': appointments,
        'today': today
    })

from .forms import OwnerForm

def owner_create(request):
    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'owner_form.html', {'form': form})

from django.shortcuts import redirect

def pet_delete(request, id):
    pet = Pet.objects.get(id=id)
    pet.delete()
    return redirect('/')

def pet_edit(request, id):
    pet = Pet.objects.get(id=id)
    form = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'pet_form.html', {'form': form})

def pet_edit(request, id):
    pet = Pet.objects.get(id=id)
    form = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'pet_form.html', {'form': form})

from .models import Veterinarian

def vets(request):
    vets = Veterinarian.objects.all()
    return render(request, 'vets.html', {'vets': vets})

from .forms import AppointmentForm
from .models import Appointment

def appointment_create(request):
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/appointments/')

    return render(request, 'appointment_form.html', {'form': form}) 

def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

from .models import MedicalRecord

def records(request):
    records = MedicalRecord.objects.all()
    return render(request, 'records.html', {'records': records})

from .models import Medicine

def medications(request):
    medications = Medicine.objects.all()
    return render(request, 'medications.html', {
        'medications': medications
    })

from .models import RecordMedication

def prescriptions(request):
    prescriptions = RecordMedication.objects.all()
    return render(request, 'prescriptions.html', {
        'prescriptions': prescriptions
    })

from .models import Appointment, MedicalRecord

def record_from_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    record = MedicalRecord.objects.create(
        pet=appointment.pet,
        vet=appointment.vet,
        diagnosis='',
        treatment='',
        visit_date=appointment.appointment_date
    )

    return redirect('/records/')

from .models import RecordMedication, Medicine

def add_prescription(request, record_id):
    record = MedicalRecord.objects.get(id=record_id)
    meds = Medicine.objects.all()

    if request.method == 'POST':
        medicine_id = request.POST.get('medicine')
        dosage = request.POST.get('dosage')

        RecordMedication.objects.create(
            record=record,
            medicine_id=medicine_id,
            dosage=dosage
        )

        return redirect('/prescriptions/')

    return render(request, 'add_prescription.html', {
        'record': record,
        'meds': meds
    })

from django.shortcuts import redirect
from .models import Appointment, MedicalRecord

def record_from_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    record = MedicalRecord.objects.create(
        pet=appointment.pet,
        vet=appointment.vet,
        diagnosis='',
        treatment='',
        visit_date=appointment.appointment_date
    )

    return redirect('/records/')

from .models import Owner

def owners(request):
    owners = Owner.objects.all()
    return render(request, 'owners.html', {'owners': owners})

from .models import Pet

def pets(request):
    pets = Pet.objects.all()
    return render(request, 'pets.html', {'pets': pets})

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def user_login(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            error = "❌ Username หรือ Password ไม่ถูกต้อง"

    return render(request, 'login.html', {'error': error})


def user_logout(request):
    logout(request)
    return redirect('login')