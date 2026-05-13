import pandas as pd
from sklearn.preprocessing import LabelEncoder

# LOAD CLEAN DATASET
df = pd.read_excel("datasets/agriculture_cleaned.xlsx")
print("Cleaned Dataset Loaded!")

# LABEL ENCODING
label_encoder = LabelEncoder()
categorical_columns = [
    "State",
    "Crop",
    "Soil_Type",
    "Fertilizer_Type"
]
for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])
print("\nCategorical columns encoded successfully!")

# DISPLAY DATA
print(df.head())

# SAVE FEATURE DATASET
df.to_excel(
    "datasets/agriculture_features.xlsx",
    index=False
)

print("\nFeature engineered dataset saved successfully!")