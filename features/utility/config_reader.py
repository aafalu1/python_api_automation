import configparser

from file_handler import FileHandler


def get_config_parser(self, filepath):
    config = configparser.ConfigParser()
    config.read(filepath)
    return config


def get_string_property(self, section, key):
    filepath = FileHandler.generate_file_path('features', 'support', file_name='config.ini')
    try:
        config = self.get_config_parser(filepath)
        return config.get(section, key)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found.")
    except configparser.Error:
        raise configparser.Error("Error occurred while parsing the config file.")


def get_boolean_property(self, section, key):
    filepath = FileHandler.generate_file_path('features', 'support', file_name='config.ini')
    try:
        config = self.get_config_parser(filepath)
        value = config.getboolean(section, key)
        return value
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found.")
    except configparser.Error:
        raise configparser.Error("Error occurred while parsing the config file.")
    except ValueError:
        raise ValueError(f"Invalid boolean value found for {section}.{key}.")


def get_integer_property(self, section, key):
    filepath = FileHandler.generate_file_path('features', 'support', file_name='config.ini')
    try:
        config = self.get_config_parser(filepath)
        value = config.get(section, key)
        if value.isdigit():
            return config.getint(section, key)
        else:
            raise ValueError(f"The value '{value}' for section '{section}' and key '{key}' is not a valid integer.")
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found.")
    except configparser.Error:
        raise configparser.Error("Error occurred while parsing the config file.")
