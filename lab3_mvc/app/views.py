from django.db.models import Sum
from django.http import HttpResponse, Http404

from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from app.models import Department, Doctor, Patient, Treatment, Procedure


def patient_page(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    template = get_template('patient_page.html')
    html = template.render({'patient': patient})
    return HttpResponse(html)
