class Crop:
    def __init__(self, name, info):
        self.name = name
        self.base_water_footprint = info['base_water_footprint']
        self.soil_preference = info['soil_preference']
        self.growing_days = info['growing_days']
        self.seasons = info['seasons']
        self.price_per_kg = info['price_per_kg']

    def __str__(self):
        return f"{self.name.capitalize()} (Growing days: {self.growing_days}, Seasons: {', '.join(self.seasons)})"
