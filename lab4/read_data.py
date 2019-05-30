import datetime
import redis
import requests

from export_configuration import ExportSourceSelector
from settings import settings


class Data:
    """
    Data class
    """
    COMPLETED_STATUS = 'COMPLETED'

    def __init__(self, url):
        """
        Initialize data

        :param url: url
        """
        self.url = url

    def read(self):
        """
        Read data from url

        :return:
        """
        rows_count = 0
        redis_db = redis.Redis(host=settings.CONFIG['REDIS_HOST'], port=settings.CONFIG['REDIS_PORT'], db=0)
        current_time = str(datetime.datetime.now())

        if redis_db.lindex(self.url, 0):
            data_status = redis_db.lindex(self.url, 0).decode('utf-8')
        else:
            data_status = ''

        if data_status == self.COMPLETED_STATUS:
            print('Try to load existing data')
        else:
            data = requests.get(self.url).json()
            redis_db.lpush(self.url, current_time)

            for row in data:
                rows_count += 1
                age_adjusted_death_rate = row.get('age_adjusted_death_rate')
                death_rate = row.get('death_rate')
                deaths = row.get('deaths')
                leading_cause = row.get('leading_cause')
                race_ethnicity = row.get('race_ethnicity')
                sex = row.get('sex')
                year = row.get('year')

                export_source = ExportSourceSelector()
                export_source.send_data(age_adjusted_death_rate, death_rate, deaths, leading_cause, race_ethnicity, sex,
                                        year, rows_count)

                if rows_count % 100 == 0:
                    redis_db.lpush(self.url, f'{rows_count - 99}-{rows_count}')
            redis_db.lpush(self.url, self.COMPLETED_STATUS)
