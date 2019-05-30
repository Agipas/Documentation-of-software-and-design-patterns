import kafka_producer
import logs
from settings import settings


class ExportSourceSelector:
    """
    Selector for export source
    """

    def __init__(self):
        """
        Initialize export type mapper for selector
        """
        self.EXPORT_TYPE_MAPPER = {
            'kafka': kafka_producer.Kafka,
            'logs': logs.Log
        }

    def send_data(self, age_adjusted_death_rate, death_rate, deaths, leading_cause, race_ethnicity, sex, year, row_id):
        export_source_name = settings.CONFIG('EXPORT_SOURCE')

        self.EXPORT_TYPE_MAPPER[export_source_name].send_data(age_adjusted_death_rate, death_rate, deaths,
                                                              leading_cause, race_ethnicity, sex, year, row_id)
