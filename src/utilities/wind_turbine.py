from typing import List
import pandas as pd
from src.helpers.config import *
from src.helpers.weather_generator import WeatherGenerator

class WindTurbine:
    def __init__(self, installed_capacity: float):
        self.installed_capacity = installed_capacity

    # Power output at a specified wind speed in MW
    def power_output_at_wind_speed (self, wind_speed) -> float:
        # Calculate power output in MW using the power curve equation
        power_curve = [0, 0, 0.125, 0.5, 1, 1.5, 2.5, 4, 6, 8, 10, 12, 14, 15, 15.5, 15.75, 16, 16]
        power_output = self.installed_capacity * power_curve[int(wind_speed)]

        return power_output

    # Power output over time in MW
    def power_output_over_time (self)-> pd.DataFrame:
        # Get hourly wind data for a year from the weather generator
        weather_generator = WeatherGenerator()
        weather_data = weather_generator.read_data()

        # Get wind speed data from the weather data (unit: m/s)
        wind_data = weather_data[get_wind_speed_header()]

        # Calculate power output for each hour of the year
        power_outputs = []
        for wind_speed in wind_data:
            power_output = self.power_output_at_wind_speed(wind_speed)
            power_outputs.append(power_output)

        # Create a DataFrame object from the power_outputs list
        return pd.DataFrame({'power_output': power_outputs})

    # Energy production over time in MWh
    def energy_production_over_time (self) -> float:
        # Calculate total energy produced by the wind turbine in a year (in MWh)
        return self.power_output_over_time().sum()