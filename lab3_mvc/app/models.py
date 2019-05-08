from django.db import models

# Create your models here.


class Procedure(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    tel = models.IntegerField()
    address = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    departmentID = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.specialization


class Patient(models.Model):
    name = models.CharField(max_length=200)
    tel = models.IntegerField()
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    date = models.DateField(max_length=200)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    procedureID = models.ManyToManyField(Procedure)

    def __str__(self):
        return str(self.date)
