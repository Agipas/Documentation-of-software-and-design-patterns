import random


class CsvGenerator:
    """
    Csv file Generator
    """
    file_name = 'generated.csv'
    names = ['Ivan', 'Petro', 'Vasyul', 'Oleg', 'Anton', 'Igor', 'Venedukt']
    departament = ['Сleaners', 'Surgeons', 'Brackets', 'Olegov', 'Antonov', 'Igorov', 'Veneduktov']

    compensations = ['Base Pay', 'Merit Pay', 'Commissions', 'Overtime Pay', 'Bonuses', 'Travel Allowance',
                     'Meal Allowance', 'Stock Options', 'Vacation Pay', 'Leaves Pay']

    projects = ['Machine learning', 'AI', 'Data Science', 'Web (Front-end)', 'Web(Back-end)',
                'Computer vision', 'AR/VR', 'Mobile', 'Desktop', 'Game Development', 'Cloud computing',
                'Computing networks', 'Administrative', 'Cryptography', 'Big Data']
    workers_count = 400
    compensations_count = 600

    def populate_compensations(self, file):
        """
        Populate compensation type into csv file

        :param file: csv file
        :return:
        """
        file.write('Compensations\n')
        for compensation in self.compensations:
            file.write('{type}\n'.format(type=compensation))

    def populate_projects(self, file):
        """
        Populate projects names into csv file

        :param file: csv file
        :return:
        """
        file.write('\nProjects\n')
        for project in self.projects:
            file.write('{name}\n'.format(name=project))

    def populate_workers(self, file):
        """
        Populate workers into csv file

        :param file: csv file
        :return:
        """
        file.write('\nWorkers\n')
        for i in range(1, self.workers_count + 1):
            worker_project = self.projects[random.randint(0, len(self.projects) - 1)]
            worker_first_name = self.names[random.randint(0, len(self.names) - 1)]
            worker_last_name = self.last_names[random.randint(0, len(self.last_names) - 1)]
            file.write('{first_name},{last_name},{projects}\n'.format(first_name=worker_first_name,
                                                                      last_name=worker_last_name,
                                                                      projects=worker_project))

    def populate_workers_compensations(self, file):
        """
        Populate workers compensations into csv file

        :param file: csv file
        :return:
        """
        file.write('\nWorkers compensations\n')
        for i in range(1, self.compensations_count + 1):
            worker_id = random.randint(1, self.workers_count + 1)
            compensation_id = random.randint(1, len(self.compensations)-1)
            amount = random.randint(0, 5000)
            file.write('{worker_id},{compensation_id},{amount}\n'.format(worker_id=worker_id,
                                                                         compensation_id=compensation_id,
                                                                         amount=amount))

    def generate_csv(self):
        """
        Generate csv file

        :return:
        """
        with open(self.file_name, 'w') as file:
            self.populate_compensations(file)
            self.populate_projects(file)
            self.populate_workers(file)
            self.populate_workers_compensations(file)


if __name__ == '__main__':
    try:
        csv_generator = CsvGenerator()
        csv_generator.generate_csv()
        print("File successfully generated")
    except:
        print("Error")
