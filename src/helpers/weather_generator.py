import pandas as pd
import numpy as np
import os

from src.helpers.config import get_weather_data_headers


class WeatherGenerator:
    def __init__(self, hours=8760, location='Netherlands'):
        self.hours = hours
        self.location = location
        self.weather_data = None

    def generate_data(self):
        # Generate hourly distribution of solar irradiation in W/m²
        solar_irradiation = np.random.normal(loc=110, scale=50, size=self.hours)
        solar_irradiation = np.clip(solar_irradiation, a_min=0, a_max=None)

        # Generate hourly distribution of temperature in °C
        temperature = np.random.normal(loc=10, scale=5, size=self.hours)

        # Generate hourly distribution of humidity in %
        humidity = np.random.normal(loc=80, scale=10, size=self.hours)
        humidity = np.clip(humidity, a_min=0, a_max=100)

        # Generate hourly distribution of wind speed in m/s
        wind_speed = np.random.normal(loc=4, scale=2, size=self.hours)
        wind_speed = np.clip(wind_speed, a_min=0, a_max=None)

        # Create hourly time index
        start_date = pd.Timestamp(year=2022, month=1, day=1, hour=0)
        time_index = pd.date_range(start=start_date, periods=self.hours, freq='H')

        solar_irradiation_header, temperature_header, humidity_header, wind_speed_header = get_weather_data_headers()

        # Combine temperature and humidity into a DataFrame
        self.weather_data = pd.DataFrame({
            solar_irradiation_header: solar_irradiation,
            temperature_header: temperature,
            humidity_header: humidity,
            wind_speed_header: wind_speed
        }, index=time_index)

    def export_data(self, file_name='data/weather_data.csv'):
        if self.weather_data is None:
            raise ValueError('Weather data not generated yet.')
        self.weather_data.to_csv(file_name)

    def read_data(self, file_name='data/weather_data.csv'):
        self.weather_data = pd.read_csv(file_name, index_col=0)
        if self.weather_data is None:
            raise ValueError('Weather data not generated yet.')
        return self.weather_data

    def print_data(self):
        self.weather_data = self.read_data()
        print(self.weather_data)