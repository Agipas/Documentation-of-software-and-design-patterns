from django.contrib import admin

# Register your models here.
from app.models import Department, Doctor, Patient, Treatment, Procedure

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Treatment)
admin.site.register(Procedure)
