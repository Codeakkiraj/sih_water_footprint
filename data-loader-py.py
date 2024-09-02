import json
from models.crop import Crop
from models.state import State
from models.soil import Soil

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_crop_data():
    data = load_json('data/crop_data.json')
    return {name: Crop(name, info) for name, info in data.items()}

def load_state_data():
    data = load_json('data/state_data.json')
    soil_data = load_soil_data()
    rainfall_data = load_json('data/rainfall_data.json')
    return {name: State(name, info, soil_data[info['primary_soil']], rainfall_data[name]) 
            for name, info in data.items()}

def load_soil_data():
    data = load_json('data/soil_data.json')
    return {name: Soil(name, info['water_retention']) for name, info in data.items()}
