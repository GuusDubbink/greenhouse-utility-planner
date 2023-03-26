import pandas as pd
from src.helpers.config import *

class SolarPanel:
    def __init__(self, efficiency):
        self.efficiency = efficiency
        self.weather_data = pd.read_csv(get_weather_data_path())

    def get_daily_average_power(self, date):
        daily_data = self.weather_data.loc[date]
        total_irradiation = daily_data[get_temperature_header()].sum() / 1000
        energy_output = total_irradiation * self.efficiency / 100
        return energy_output / 24

    def get_power_at_time(self, datetime):
        hour_data = self.weather_data.loc[datetime]
        total_irradiation = hour_data[get_temperature_header()] / 1000
        energy_output = total_irradiation * self.efficiency / 100
        return energy_output



# Create a SolarPanel object with efficiency of 20% and weather data file "weather_data.csv"
panel = SolarPanel(efficiency=20)

# Get daily average power output for March 1, 2023
daily_average_power = panel.get_daily_average_power("2023-03-01")
print("Daily average power output on March 1, 2023: {:.2f} kWh".format(daily_average_power))

# Get power output at 12:00 pm on March 1, 2023
power_at_noon = panel.get_power_at_time("2023-03-01 12:00:00")
print("Power output at 12:00 pm on March 1, 2023: {:.2f} kWh".format(power_at_noon))
