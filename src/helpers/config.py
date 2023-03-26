import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

# Read database connection parameters from config file
def get_database_config():
    host = config.get('database', 'host')
    user = config.get('database', 'user')
    password = config.get('database', 'password')
    database = config.get('database', 'database')

    return host, user, password, database

def get_weather_data_path():
    folder_path = config.get('weather', 'folder_path')
    filename = config.get('weather', 'filename')
    return os.path.join(folder_path, filename)

def get_weather_data_headers():
    solar_irradiation_header = config.get('weather', 'solar_irradiation_header')
    temperature_header = config.get('weather', 'temperature_header')
    humidity_header = config.get('weather', 'humidity_header')
    wind_speed_header = config.get('weather', 'wind_speed_header')
    return solar_irradiation_header, temperature_header, humidity_header, wind_speed_header

def get_temperature_header():
    return config.get('weather', 'temperature_header')

def get_wind_speed_header():
    return config.get('weather', 'wind_speed_header')
