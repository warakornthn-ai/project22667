from django import forms
from .models import Appointment, Owner, Pet
# ฟอร์มจองคิว
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'vet', 'appointment_date', 'status', 'note']
        widgets = {
            'appointment_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            )
        }

    # 🔥 เพิ่มตัวนี้ (สำคัญมาก)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appointment_date'].input_formats = ['%Y-%m-%dT%H:%M']


# ฟอร์มเจ้าของ (เพิ่มใหม่)
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'phone', 'email', 'address']

from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['owner', 'name', 'species', 'breed', 'gender', 'birthdate']