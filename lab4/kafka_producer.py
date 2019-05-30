import json
from kafka import KafkaProducer
from time import sleep

from export_source import ExportSource
from settings import settings


class Kafka(ExportSource):
    """
    Kafka class
    """

    def __init__(self):
        super(ExportSource, self).__init__()

    @staticmethod
    def send_data(age_adjusted_death_rate, death_rate, deaths, leading_cause, race_ethnicity, sex, year, row_id):
        """

        :param age_adjusted_death_rate:
        :param death_rate:
        :param deaths:
        :param leading_cause:
        :param race_ethnicity:
        :param sex:
        :param year:
        :param row_id:
        :return:
        """

        producer = KafkaProducer(
            bootstrap_servers=[f"{settings.CONFIG['KAFKA_HOST']}:{settings.CONFIG['KAFKA_PORT']}"],
            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        data = {'id': row_id,
                'age_adjusted_death_rate': age_adjusted_death_rate,
                'death_rate': death_rate,
                'deaths': deaths,
                'leading_cause': leading_cause,
                'race_ethnicity': race_ethnicity,
                'sex': sex,
                'year': year}
        topic_name = 'lab4'
        #
        # if settings.CONFIG['KAFKA_TOPIC_ID'] == 1:
        #     topic_name = 'lab4'
        # else:
        #     topic_name = 'topic2'
        producer.send(topic_name, data)
        sleep(0.1)
