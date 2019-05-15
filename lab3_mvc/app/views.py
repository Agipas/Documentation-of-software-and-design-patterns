import os
import re
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


def read_csv_file(request):
    """
    Read csv file and insert data to db

    :param request: WSGI request
    :return: http response
    """
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'generated.csv')
    with open(file_path, 'r+') as file:
        buffer = file.read()
        first = re.split(r'Departments\n', buffer)[1]
        sec = re.split(r'.*\nProcedures\n', first)[0]
        departments = sec.split('\n')
        for department in departments:
            if department != '':
                Department.objects.get_or_create(name=department)

    first = re.split(r'Procedures\n', buffer)[1]
    sec = re.split(r'.*\nDoctors\n', first)[0]
    procedures = sec.split('\n')
    for procedure in procedures:
        if procedure != '':
            procedure_detail = procedure.split(',')
            Procedure.objects.get_or_create(name=procedure_detail[0],
                                            price=procedure_detail[1])

    first = re.split(r'Doctors\n', buffer)[1]
    sec = re.split(r'.*\nPatients\n', first)[0]
    doctors = sec.split('\n')
    for doctor in doctors:
        if doctor != '':
            doctor_detail = doctor.split(',')
            Doctor.objects.get_or_create(name=doctor_detail[0],
                                         tel=doctor_detail[1],
                                         address=doctor_detail[2],
                                         specialization=doctor_detail[3],
                                         departmentID=Department.objects.get(id=int(doctor_detail[4])))

    first = re.split(r'Patients\n', buffer)[1]
    sec = re.split(r'.*\nTreatments\n', first)[0]
    patients = sec.split('\n')
    for patient in patients:
        if patient != '':
            patient_detail = patient.split(',')
            try:
                Patient.objects.get_or_create(name=patient_detail[0],
                                              tel=patient_detail[1],
                                              address=patient_detail[2],
                                              age=patient_detail[3],
                                              sex=patient_detail[4],
                                              doctorID=Doctor.objects.get(id=patient_detail[5]))
            except:
                pass

    first = re.split(r'Treatments\n', buffer)[1]
    treatments = first.split('\n')
    for treatment in treatments:
        if treatment != '':
            treatment_detail = treatment.split(',')
            procedures = Procedure.objects.get(id=treatment_detail[1])
            treat = Treatment(patientID=Patient.objects.get(id=treatment_detail[0]),
                              date=treatment_detail[2])
            treat.save()
            treat.procedureID.add()
            treat.procedureID.add(procedures)
            # for procedure in procedures:
                # treatment_data = Treatment.objects.get(patientID=Patient.objects.get(id=treatment_detail[0]),
                #                                    date=treatment_detail[2])
                # treat.procedureID.add(procedure)

    return HttpResponse('<html><h1>SUCCESS</h1></html>')
