import localconfig
from attrdict import AttrDict


class Settings:
    """
    Settings class
    """
    CONFIG = None

    def __init__(self, file_name='server.conf'):
        """
        Initialize config
        """
        self.read_conf_file(file_name)

    def read_conf_file(self, file_name, config_group='lab'):
        """
        Read data from configuration file

        :param file_name: file name
        :param config_group: config group
        :return:
        """
        with open(file_name, 'r') as f:
            config_string = f.read()

        config = localconfig.LocalConfig()
        config.read(config_string)

        params = AttrDict({str(key).upper(): value for key, value in getattr(config, config_group) or {}})

        self.CONFIG = params


settings = Settings()
