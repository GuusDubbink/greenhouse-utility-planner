from src.helpers.weather_generator import WeatherGenerator

# weather = WeatherGenerator(hours=8760)
# weather.generate_data()
# weather.export_data()
# weather.read_data()
# weather.get_hourly_data()
from src.utilities.wind_turbine import WindTurbine

wind = WindTurbine(installed_capacity=5)
power = wind.power_output_over_time()
print(power.head())