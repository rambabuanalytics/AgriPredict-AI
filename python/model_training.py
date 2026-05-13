import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# LOAD FEATURE DATASET
df = pd.read_excel(
    "datasets/agriculture_features.xlsx"
)
print("Feature Dataset Loaded!")

# FEATURES & TARGET
X = df.drop("Yield", axis=1)
y = df["Yield"]

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTrain Test Split Done!")

# MODEL TRAINING
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)
print("\nModel Training Completed!")

# PREDICTIONS
predictions = model.predict(X_test)

# EVALUATION
r2 = r2_score(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
print("\nModel Evaluation Metrics:\n")
print(f"R2 Score: {round(r2, 3)}")
print(f"Mean Squared Error (MSE): {round(mse, 2)}")

# SAVE MODEL
joblib.dump(
    model,
    "models/crop_yield_model.pkl"
)
print("\nModel Saved Successfully!")