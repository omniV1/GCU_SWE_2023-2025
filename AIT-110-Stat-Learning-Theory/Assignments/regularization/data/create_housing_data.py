"""
Create housing dataset with required columns for regularization assignment.
Adapts USA Housing dataset from linear-regression assignment.
"""
import pandas as pd
import numpy as np
from pathlib import Path

# Load USA Housing dataset
base_path = Path(__file__).resolve().parent.parent.parent / "linear-regression" / "data"
df = pd.read_excel(base_path / "usa_housing_dataset.xls", sheet_name="Data")

# Create required columns
housing = pd.DataFrame()
housing["Price"] = df["price"]
housing["Size"] = df["sqft_living"]
housing["Bedrooms"] = df["bedrooms"]
housing["Year_built"] = df["yr_built"]
housing["Age"] = 2026 - df["yr_built"]
housing["Lot_size"] = df["sqft_lot"]
housing["Bathrooms"] = df["bathrooms"]

# Distance_to_city_center: synthetic - larger lots often further from city center
np.random.seed(42)
base_dist = 5 + (housing["Lot_size"] / 10000) * 2
housing["Distance_to_city_center"] = np.clip(
    base_dist + np.random.normal(0, 3, len(housing)), 1, 50
)

# Garage: synthetic - correlated with bedrooms and size (larger homes more likely to have garage)
garage_prob = 0.3 + 0.1 * housing["Bedrooms"] + 0.00002 * housing["Size"]
housing["Garage"] = (np.random.uniform(0, 1, len(housing)) < np.clip(garage_prob, 0, 1)).astype(int)

# Drop any rows with missing values
housing = housing.dropna()

# Save to CSV
output_path = Path(__file__).resolve().parent / "housing_prices.csv"
housing.to_csv(output_path, index=False)
print(f"Saved {len(housing)} records to {output_path}")
