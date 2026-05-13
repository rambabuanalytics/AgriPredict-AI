import pandas as pd

# LOAD DATASET
df = pd.read_csv("datasets/agriculture_dataset.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# CHECK NULL VALUES

print("\nMissing Values:\n")
print(df.isnull().sum())

# REMOVE DUPLICATES
df = df.drop_duplicates()

# CLEAN COLUMN NAMES
df.columns = df.columns.str.strip()

# DATA TYPES
print("\nDataset Info:\n")
print(df.info())

# SAVE CLEAN DATASET
df.to_excel(
    "datasets/agriculture_cleaned.xlsx",
    index=False
)

print("\nCleaned dataset saved successfully!")