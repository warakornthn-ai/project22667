from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)

admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Veterinarian)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Medicine)
admin.site.register(RecordMedication)

admin.site.site_header = "🐾 PET CLINIC ADMIN"
admin.site.site_title = "PET CLINIC ADMIN"
admin.site.index_title = "ระบบจัดการคลินิกสัตว์"