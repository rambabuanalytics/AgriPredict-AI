import joblib

from utils import preprocess_input
from utils import format_prediction

from config import MODEL_PATH

# LOAD MODEL

try:
    model = joblib.load(MODEL_PATH)

except:
    model = None

# PREDICTION FUNCTION

def predict_yield(
    state,
    crop,
    rainfall,
    temperature,
    humidity,
    soil,
    fertilizer
):

    input_df = preprocess_input(
        state,
        crop,
        rainfall,
        temperature,
        humidity,
        soil,
        fertilizer
    )

    # REAL MODEL PREDICTION

    if model:

        prediction = model.predict(input_df)[0]

        return format_prediction(prediction)


    # DUMMY PREDICTION

    return 114.01