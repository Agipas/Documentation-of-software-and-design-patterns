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
        first = re.split(r'Compensations\n', buffer)[1]
        sec = re.split(r'.*\n\nProjects\n', first)[0]
        compensations = sec.split('\n')
        for compensation in compensations:
            if compensation!='':
                Compensation.objects.get_or_create(
                    type=compensation
                )

        first = re.split(r'Projects\n', buffer)[1]
        sec = re.split(r'.*\nWorkers\n', first)[0]
        projects = sec.split('\n')
        for project in projects:
            if project!='':
                Project.objects.get_or_create(
                    name=project
                )

    first = re.split(r'Workers\n', buffer)[1]
    sec = re.split(r'.*\n\nWorkers compensations\n', first)[0]
    workers = sec.split('\n')
    for worker in workers:
        if worker != '':
            worker_details = worker.split(',')
            worker_project = Project.objects.get(name=worker_details[2])
            worker = Worker(
                first_name=worker_details[0],
                last_name=worker_details[1],
            )
            worker.save()
            worker.projects.add(worker_project)

    first = re.split(r'Workers compensations\n', buffer)[1]
    workers_compensations = first.split('\n')
    for worker_compensation in workers_compensations:
        if worker_compensation != '':
            worker_compensation_detail = worker_compensation.split(',')
            try:
                WorkerCompensation.objects.get_or_create(worker_id=worker_compensation_detail[0],
                                                         compensation_type_id=worker_compensation_detail[1],
                                                         amount=worker_compensation_detail[2])
            except:
                pass

    return HttpResponse('<html><h1>SUCCESS</h1></html>')