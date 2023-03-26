class Greenhouse:
    def __init__(self, location="Rotterdam", area=1000, crop="tomato", greenhouse_type="glass"):
        self.location = location
        self.area = area
        self.crop = crop
        self.greenhouse_type = greenhouse_type
        self.demand_heat = []
        self.demand_cooling = []
        self.demand_lighting = []
        self.demand_ventilation = []
        self.demand_irrigation = []
        self.crop_yield = []
        self.crop_production = []
        self.revenue = []

    def calculate_demand(self, solar_irradiation, temperature, humidity, wind_speed, operation_schedule):
        # Calculate demand for heat, cooling, lighting, ventilation, and irrigation
        # based on the crop type, weather conditions, the greenhouse type, and operation strategy.
        # Store the demand in the appropriate variables.
        pass

    def calculate_crop_yield(self):
        # Calculate the crop yield based on the demand for heat, cooling, lighting, ventilation,
        # and irrigation, and the crop type.
        # Store the crop yield in the appropriate variable.
        pass

    def calculate_crop_production(self):
        # Calculate the crop production based on the crop yield and the area of the greenhouse.
        # Store the crop production in the appropriate variable.
        pass

    def calculate_revenue(self, price):
        # Calculate the revenue based on the crop production and the price per unit of crop.
        # Store the revenue in the appropriate variable.
        pass
