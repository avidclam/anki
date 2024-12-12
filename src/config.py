from collections import UserDict
from collections.abc import Mapping
import tomllib
from dotenv import dotenv_values


defaults = {
    'ingest.dotenv_key': 'SOURCE_TSV'
}


class Config(UserDict):
    def get_path(self, path: str, default=None, *, sep='.'):
        """
        Access nested configuration values using dot-separated paths.

        :param path: The dot-separated path to the desired key.
        :param default: The default value to return if the path is not found.
        :param sep: Override dot with a different separator.
        :return: The value at the specified path or the default value.
        """
        keys = path.split(sep)
        value = self.data
        for key in keys:
            if isinstance(value, Mapping) and key in value:
                value = value[key]
            else:
                return default
        return value


# Function to load the TOML configuration file
def load_config(file_path):
    try:
        with open(file_path, "rb") as f:
            config = Config(tomllib.load(f))
    except FileNotFoundError:
            config = Config()

    # Check if input path needs to be loaded from .env
    use_dotenv = config.get_path('ingest.use_dotenv', True)
    if use_dotenv:
        dotenv_config = dotenv_values()
        dotenv_key = config.get_path('ingest.dotenv_key',
                                     default=defaults['ingest.dotenv_key'])
        if not (dotenv_key and dotenv_key in dotenv_config):
            raise ValueError('Cannot use .env for loading input')
        if 'ingest' not in config:
            config['ingest'] = {}
        config['ingest']['file_path'] = dotenv_config[dotenv_key]

    return config