# Import required libraries
import pandas as pd
import os

# ---------------------------------------------------------
# Step 1: Load the dataset
# ---------------------------------------------------------
# Define the absolute path to the raw dataset (use raw string format to avoid escape issues)
raw_data_path = r"C:\Users\Kmmadu\Churn-Prediction-PowerBI\data\WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Read the dataset into a Pandas DataFrame
df = pd.read_csv(raw_data_path)

# ---------------------------------------------------------
# Step 2: Clean 'TotalCharges' column (it contains spaces or non-numeric values)
# ---------------------------------------------------------
# Replace blank spaces with NaN
df['TotalCharges'] = df['TotalCharges'].replace(" ", pd.NA)

# Convert 'TotalCharges' to numeric (will raise error if non-numeric remains)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# ---------------------------------------------------------
# Step 3: Handle missing values
# ---------------------------------------------------------
# Drop rows with missing 'TotalCharges'
df.dropna(subset=['TotalCharges'], inplace=True)

# ---------------------------------------------------------
# Step 4: Standardize 'No internet service' → 'No' in service columns
# ---------------------------------------------------------
internet_cols = [
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Apply the replacement
df[internet_cols] = df[internet_cols].replace('No internet service', 'No')

# ---------------------------------------------------------
# Step 5: Standardize 'No phone service' → 'No' in 'MultipleLines'
# ---------------------------------------------------------
df['MultipleLines'] = df['MultipleLines'].replace('No phone service', 'No')

# ---------------------------------------------------------
# Step 6: Convert 'SeniorCitizen' from 0/1 → 'No'/'Yes'
# ---------------------------------------------------------
df['SeniorCitizen'] = df['SeniorCitizen'].replace({1: 'Yes', 0: 'No'})

# ---------------------------------------------------------
# Step 7: Drop 'customerID' (not relevant for analysis)
# ---------------------------------------------------------
df.drop(columns='customerID', inplace=True)

# ---------------------------------------------------------
# Step 8: Export cleaned data to a new CSV
# ---------------------------------------------------------
# Define output path
output_folder = os.path.join(os.path.dirname(__file__), "cleaned_data")
os.makedirs(output_folder, exist_ok=True)

cleaned_path = os.path.join(output_folder, "telco_cleaned.csv")
df.to_csv(cleaned_path, index=False)

# ---------------------------------------------------------
# Step 9: Confirm success
# ---------------------------------------------------------
print("Absolute path:", os.path.abspath(cleaned_path))
print(f"Cleaned data saved to: {cleaned_path}")
