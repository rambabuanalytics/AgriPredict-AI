import pandas as pd

# ENCODING MAPS

state_map = {
    "Delhi": 0,
    "Punjab": 1,
    "Haryana": 2,
    "Gujarat": 3,
    "Bihar": 4,
    "Rajasthan": 5,
    "Maharashtra": 6,
    "Tamil Nadu": 7,
    "Uttar Pradesh": 8,
    "Madhya Pradesh": 9,
    "Goa": 10,
    "Kerala": 11,
    "Karnataka": 12,
    "Assam": 13,
    "Jharkhand": 14,
    "West Bengal": 15,
    "Odisha": 16,
    "Chhattisgarh": 17,
    "Telangana": 18,
    "Andhra Pradesh": 19,
    "Arunachal Pradesh": 20,
    "Nagaland": 21,
    "Manipur": 22,
    "Mizoram": 23,
    "Tripura": 24,
    "Meghalaya": 25,
    "Sikkim": 26,
    "Himachal Pradesh": 27
}

crop_map = {
    "Rice": 0,
    "Wheat": 1,
    "Cotton": 2,
    "Sugarcane": 3,
    "Maize": 4,
    "Barley": 5,
    "Pulses": 6,
    "Bajra": 7,
    "Millets": 8,
    "Jowar": 9
}

soil_map = {
    "Black": 0,
    "Red": 1,
    "Alluvial": 2,
    "Laterite": 3,
    "Mountain": 4,
    "Desert": 5
}

fertilizer_map = {
    "Urea": 0,
    "DAP": 1,
    "Compost": 2,
    "Organic": 3,
    "MOP": 4
}

# PREPROCESS INPUT

def preprocess_input(
    state,
    crop,
    rainfall,
    temperature,
    humidity,
    soil,
    fertilizer
):

    data = {
        "State": [state_map[state]],
        "Crop": [crop_map[crop]],
        "Rainfall": [rainfall],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Soil_Type": [soil_map[soil]],
        "Fertilizer_Type": [fertilizer_map[fertilizer]]
    }

    df = pd.DataFrame(data)

    return df

# FORMAT PREDICTION

def format_prediction(value):

    return round(value, 2)