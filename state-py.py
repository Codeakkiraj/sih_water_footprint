class State:
    def __init__(self, name, info, primary_soil, rainfall_data):
        self.name = name
        self.climate_factor = info['climate_factor']
        self.primary_soil = primary_soil
        self.electricity_cost = info['electricity_cost']
        self.rainfall_data = rainfall_data

    def get_rainfall_data(self):
        return self.rainfall_data

    def __str__(self):
        return f"{self.name.capitalize()} (Climate factor: {self.climate_factor}, Primary soil: {self.primary_soil.name})"
