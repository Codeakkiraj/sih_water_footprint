from datetime import datetime, timedelta

def calculate_water_footprint(crop, state, land_size):
    base_footprint = crop.base_water_footprint
    climate_factor = state.climate_factor
    primary_soil = state.primary_soil
    soil_factor = primary_soil.water_retention

    # Adjust water footprint based on soil preference
    soil_suitability = 1.0 if primary_soil.name in crop.soil_preference else 1.2

    # Calculate water footprint per hectare
    water_footprint = base_footprint * climate_factor * soil_factor * soil_suitability * land_size

    # Adjust for rainfall
    rainfall_data = state.get_rainfall_data()
    total_rainfall = sum(rainfall_data.values())
    water_footprint = max(0, water_footprint - (total_rainfall * land_size))

    return {
        "water_footprint": water_footprint,
        "soil_type": primary_soil.name,
        "rainfall": total_rainfall
    }

def create_irrigation_schedule(water_needed, land_size, crop):
    weeks = min(5, crop.growing_days // 7)  # Schedule for up to 5 weeks or until crop maturity
    water_per_week = water_needed / weeks
    schedule = []
    start_date = datetime.now()
    for i in range(weeks):
        date = start_date + timedelta(days=i*7)
        schedule.append({
            "week": i + 1,
            "date": date.strftime("%Y-%m-%d"),
            "water_liters": round(water_per_week, 2)
        })
    return schedule

def calculate_pump_time(water_liters, pump_flow_rate):
    hours = water_liters / pump_flow_rate
    return round(hours, 2)

def estimate_yield(crop, land_size):
    # This is a simplified yield estimation. In a real-world scenario,
    # you'd need more complex models considering various factors.
    base_yield = 2000  # kg per hectare
    return base_yield * land_size

def calculate_profit(crop, yield_kg, water_used, electricity_cost):
    revenue = yield_kg * crop.price_per_kg
    water_cost = water_used * 0.001  # Assuming 0.001 INR per liter of water
    electricity_used = water_used / 1000  # Assuming 1 kWh pumps 1000 liters
    electricity_cost = electricity_used * electricity_cost
    total_cost = water_cost + electricity_cost
    profit = revenue - total_cost
    return {
        "revenue": revenue,
        "water_cost": water_cost,
        "electricity_cost": electricity_cost,
        "total_cost": total_cost,
        "profit": profit
    }
