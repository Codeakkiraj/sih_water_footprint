class Soil:
    def __init__(self, name, water_retention):
        self.name = name
        self.water_retention = water_retention

    def __str__(self):
        return f"{self.name.capitalize()} soil (Water retention: {self.water_retention})"
