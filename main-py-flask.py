from flask import Flask, render_template, request, jsonify
from utils.calculations import calculate_water_footprint, create_irrigation_schedule, calculate_pump_time, estimate_yield, calculate_profit
from utils.data_loader import load_crop_data, load_state_data, load_soil_data
from models.crop import Crop
from models.state import State

app = Flask(__name__)

# Load data
crops = load_crop_data()
states = load_state_data()
soils = load_soil_data()

@app.route('/')
def home():
    return render_template('index.html', crops=crops.keys(), states=states.keys())

@app.route('/calculate', methods=['POST'])
def calculate():
    crop_name = request.form['crop']
    state_name = request.form['state']
    land_size = float(request.form['land_size'])
    pump_flow_rate = float(request.form['pump_flow_rate'])

    crop = crops[crop_name]
    state = states[state_name]

    result = calculate_water_footprint(crop, state, land_size)
    schedule = create_irrigation_schedule(result['water_footprint'], land_size, crop)
    
    estimated_yield = estimate_yield(crop, land_size)
    profit_info = calculate_profit(crop, estimated_yield, result['water_footprint'], state.electricity_cost)

    return jsonify({
        'water_footprint': result['water_footprint'],
        'soil_type': result['soil_type'],
        'rainfall': result['rainfall'],
        'schedule': schedule,
        'estimated_yield': estimated_yield,
        'profit_info': profit_info
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
