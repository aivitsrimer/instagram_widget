import os
import sys

from configparser import ConfigParser


class ApplicationSettings:
    _access_token = '20261245390.1677ed0.f9d9fd4ebb134fde90dc9ef54d443fa8'
    _organization_name = 'Project'
    _config_file_name = 'instagram_widget.conf'
    _db_name = 'instagram.db'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self._config = ConfigParser()

        if not os.path.exists(self._local_config_path()):
            self._create_default_local_config()

        self._config.read(self._local_config_path())

    @property
    def token(self) -> str:
        return self._get_value('General', 'token')

    @property
    def db_name(self) -> str:
        return self._get_value('General', 'db_name')

    def _create_default_local_config(self):
        self._config['General'] = {}
        self._config['General']['token'] = self._access_token
        self._config['General']['db_name'] = self._db_name

        path = self._local_config_path()
        basedir = os.path.dirname(path)

        if not os.path.exists(basedir):
            os.makedirs(basedir)

        with open(path, 'w') as config_file:
            self._config.write(config_file)

    def _get_value(self, section, key):
        try:
            return self._config[section][key]
        except KeyError:
            print('Invalid application settings file')
            sys.exit(1)

    @staticmethod
    def _home_directory():
        return os.path.expanduser('~')

    @classmethod
    def _local_config_path(cls):
        return os.path.join(
            cls._home_directory(),
            '.config',
            cls._organization_name,
            cls._config_file_name
        )


application_settings = ApplicationSettings()
