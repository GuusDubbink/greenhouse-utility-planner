from src.helpers.weather_generator import WeatherGenerator
from src.utilities.solar_panel import SolarPanel

# weather = WeatherGenerator(hours=8760)
# weather.generate_data()
# weather.export_data()
# weather.read_data()
# weather.get_hourly_data()

solar = SolarPanel(efficiency=20)
daily_average_power = solar.get_daily_average_power("2023-03-01")