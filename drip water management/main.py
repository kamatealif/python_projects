import pandas as pd

def calculate_water_requirement(crop_type, soil_type, area_acres):
    water_needs = {
        'wheat': 5,  # mm per day
        'rice': 7,
        'corn': 6,
        'vegetables': 4
    }
    
    soil_factor = {
        'sandy': 1.2,
        'loamy': 1.0,
        'clay': 0.8
    }
    
    if crop_type not in water_needs or soil_type not in soil_factor:
        raise ValueError("Invalid crop type or soil type")
    
    daily_water_mm = water_needs[crop_type] * soil_factor[soil_type]
    daily_water_liters = daily_water_mm * area_acres * 4046.86  # Convert mm to liters
    return daily_water_liters

def save_to_excel(data, filename='water_management.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    crop = input("Enter crop type (wheat/rice/corn/vegetables): ").strip().lower()
    soil = input("Enter soil type (sandy/loamy/clay): ").strip().lower()
    area = float(input("Enter field area in acres: "))
    
    water_required = calculate_water_requirement(crop, soil, area)
    print(f"Daily water requirement: {water_required:.2f} liters")
    
    data = [{
        'Crop': crop,
        'Soil Type': soil,
        'Area (acres)': area,
        'Daily Water Requirement (liters)': water_required
    }]
    
    save_to_excel(data)
