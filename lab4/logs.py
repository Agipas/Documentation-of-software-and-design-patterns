import logging

from export_source import ExportSource


class Log(ExportSource):
    """
    Log class
    """
    def __init__(self):
        super(ExportSource, self).__init__()

    @staticmethod
    def send_data(age_adjusted_death_rate, death_rate, deaths, leading_cause, race_ethnicity,
                 sex, year, row_id):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.info(f'LOG DATA FOR {row_id} ROW')
        logging.info(f'AGE ADJUSTED DEATH RATE={age_adjusted_death_rate}')
        logging.info(f'DATE RATE={death_rate}')
        logging.info(f'DEATHS={deaths}')
        logging.info(f'LOADING CAUSE={leading_cause}')
        logging.info(f'RACE ETHNICITY={race_ethnicity}')
        logging.info(f'SEX={sex}')
        logging.info(f'YEAR={year}')
        logging.info('.............................................................')
