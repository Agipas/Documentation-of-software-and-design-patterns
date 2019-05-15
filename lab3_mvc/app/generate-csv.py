import random
from datetime import date


class CsvGenerator:
    """
    Csv file Generator
    """
    file_name = 'generated.csv'

    procedure_names = ['Cleaning', 'Tooth extraction', 'Bracket insertion', 'Whitening', 'X-ray', 'Review',
                       'Tooth Restoration']

    departments = ['Cleaners', 'Surgeons', 'Brackets', "Childrens_dentist"]

    doctors_names = ['Ivan', 'Petro', 'Vasyul', 'Oleg', 'Anton', 'Igor', 'Venedukt']
    address = ['Lviv', 'Kyev', 'Khmelnitskyi', 'Ternopil', 'Zakarpattia', 'Donetsk']
    specialization = ['Dentist', 'Surgeon', 'Cleaner']

    patient_names = ['Anton', 'Dima', 'Vova', 'Bogdan', 'Bob', 'Jek', 'John']
    patient_address = ['Moscow', 'Tokyo', 'London', 'Ternopil', 'Rivne', 'Donetsk']

    patient_count = 200
    treatments_count = 800

    def populate_department(self, file):
        """
        Populate Department type into csv file

        :param file: csv file
        :return:
        """
        file.write('Departments\n')
        for department in self.departments:
            file.write('{name}\n'.format(name=department))

    def populate_procedure(self, file):
        """
        Populate Procedure names into csv file

        :param file: csv file
        :return:
        """
        file.write('\nProcedures\n')
        for procedure in self.procedure_names:
            price = random.randint(100, 500)
            file.write('{name},{price}\n'.format(name=procedure,
                                                 price=price))

    def populate_doctor(self, file):
        """
        Populate Doctor into csv file

        :param file: csv file
        :return:
        """
        file.write('\nDoctors\n')
        for doctor in self.doctors_names:
            tel = random.randint(100000000, 999999999)
            # worker_project = self.projects[random.randint(0, len(self.doctors_names) - 1)]
            doctor_address = self.address[random.randint(0, len(self.address) - 1)]
            doctor_specialization = self.specialization[random.randint(0, len(self.specialization) - 1)]
            department_id = random.randint(1, len(self.departments) - 1)
            file.write('{name},{tel},{address},{specialization},{departmentID}\n'.format(name=doctor,
                                                                                         tel='0' + str(tel),
                                                                                         address=doctor_address,
                                                                                         specialization=doctor_specialization,
                                                                                         departmentID=department_id))

    def populate_patient(self, file):
        """
        Populate Patient into csv file

        :param file: csv file
        :return:
        """
        file.write('\nPatients\n')
        for i in range(1, self.patient_count + 1):
            tel = random.randint(100000000, 999999999)
            age = random.randint(18, 60)
            patient_names = self.patient_names[random.randint(0, len(self.patient_names) - 1)]
            patient_address = self.patient_address[random.randint(0, len(self.patient_address) - 1)]
            doctor_id = random.randint(1, len(self.doctors_names) - 1)
            file.write('{name},{tel},{address},{age},{sex},{doctorID}\n'.format(name=patient_names,
                                                                                tel='0' + str(tel),
                                                                                address=patient_address,
                                                                                age=age,
                                                                                sex='male',
                                                                                doctorID=doctor_id))

    def populate_treatment(self, file):
        """
        Populate Treatments compensations into csv file

        :param file: csv file
        :return:
        """
        file.write('\nTreatments\n')
        for i in range(1, self.treatments_count + 1):
            patient_id = random.randint(1, self.patient_count)
            procedure_id = random.randint(1, len(self.procedure_names))
            day = random.randint(1, 28)
            file.write('{patientID},{procedureID},{date}\n'.format(patientID=patient_id,
                                                                   procedureID=procedure_id,
                                                                   date='2019-03-' + str(day)))

    def generate_csv(self):
        """
        Generate csv file

        :return:
        """
        with open(self.file_name, 'w') as file:
            self.populate_department(file)
            self.populate_procedure(file)
            self.populate_doctor(file)
            self.populate_patient(file)
            self.populate_treatment(file)


if __name__ == '__main__':
    try:
        csv_generator = CsvGenerator()
        csv_generator.generate_csv()
        print("File successfully generated")
    except:
        print("Error")
