from django.db import models
from django.db.models import Q
from datetime import date

# 👤 เจ้าของสัตว์
class Owner(models.Model):
    owner_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.owner_id:
            last_owner = Owner.objects.order_by('-id').first()
            if last_owner:
                last_id = int(last_owner.owner_id[1:])
                new_id = f"A{last_id+1:04d}"
            else:
                new_id = "A0001"
            self.owner_id = new_id

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner_id} - {self.name}"


# 🐶 สัตว์เลี้ยง
class Pet(models.Model):
    pet_id = models.CharField(max_length=10, unique=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pet_id:
            last_pet = Pet.objects.order_by('-id').first()

            if last_pet and last_pet.pet_id and last_pet.pet_id.startswith('P'):
                try:
                    last_id = int(last_pet.pet_id[1:])
                    new_id = f"P{last_id+1:03d}"
                except:
                    new_id = "P001"
            else:
                new_id = "P001"

            self.pet_id = new_id

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pet_id} - {self.name}"

    # 🔥 เพิ่มอายุ
    def get_age(self):
        today = date.today()
        years = today.year - self.birthdate.year
        months = today.month - self.birthdate.month

        if months < 0:
            years -= 1
            months += 12

        return f"{years} ปี {months} เดือน" 

# 👨‍⚕️ สัตวแพทย์
class Veterinarian(models.Model):
    vet_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.vet_id:
            last = Veterinarian.objects.order_by('-id').first()
            if last and last.vet_id.startswith('V'):
                try:
                    num = int(last.vet_id[1:])
                    new_id = f"V{num+1:04d}"
                except:
                    new_id = "V0001"
            else:
                new_id = "V0001"
            self.vet_id = new_id

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.vet_id} - {self.name}"


# 📅 นัดหมาย
class Appointment(models.Model):
    appointment_id = models.CharField(max_length=10, unique=True, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    note = models.TextField()

    def save(self, *args, **kwargs):
        if not self.appointment_id:
            last = Appointment.objects.order_by('-id').first()
            if last and last.appointment_id.startswith('AP'):
                try:
                    num = int(last.appointment_id[2:])
                    self.appointment_id = f"AP{num+1:03d}"
                except:
                    self.appointment_id = "AP001"
            else:
                self.appointment_id = "AP001"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.appointment_id

# 🩺 ประวัติการรักษา
class MedicalRecord(models.Model):
    record_id = models.CharField(max_length=10, unique=True, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255)
    treatment = models.TextField()
    visit_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.record_id:
            last = MedicalRecord.objects.order_by('-id').first()
            if last and last.record_id.startswith('R'):
                try:
                    num = int(last.record_id[1:])
                    self.record_id = f"R{num+1:03d}"
                except:
                    self.record_id = "R001"
            else:
                self.record_id = "R001"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.record_id

    # 🔥 เพิ่มตรงนี้
    @staticmethod
    def search(query):
        return MedicalRecord.objects.filter(
            Q(pet__name__icontains=query) |
            Q(pet__pet_id__icontains=query) |
            Q(pet__owner__name__icontains=query) |
            Q(pet__owner__owner_id__icontains=query) |
            Q(record_id__icontains=query) |
            Q(vet__name__icontains=query)
        )


# 💊 ยา / วัคซีน
class Medicine(models.Model):
    med_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.med_id:
            last = Medicine.objects.order_by('-id').first()
            if last and last.med_id.startswith('M'):
                try:
                    num = int(last.med_id[1:])
                    self.med_id = f"M{num+1:03d}"
                except:
                    self.med_id = "M001"
            else:
                self.med_id = "M001"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.med_id} - {self.name}"


# 🔗 การใช้ยา
class RecordMedication(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.record.record_id} - {self.medicine.name}"