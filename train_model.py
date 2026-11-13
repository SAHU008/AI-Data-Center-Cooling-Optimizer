
import csv
import json
import numpy as np

# Load dataset
with open("data/server_data.csv", "r") as file:
    reader = csv.DictReader(file)
    records = list(reader)

# Input features
features = [
    "cpu_usage",
    "ambient_temp",
    "inlet_temp",
    "airflow",
    "cooling_power"
]

X = np.array([
    [float(row[col]) for col in features]
    for row in records
])

# Target: server temperature
y = np.array([
    float(row["server_temp"])
    for row in records
])

# Split data: 80% training, 20% testing
split = int(0.8 * len(X))

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Normalize features using training data
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)
std[std == 0] = 1

X_train_scaled = (X_train - mean) / std
X_test_scaled = (X_test - mean) / std

# Add intercept column
X_train_scaled = np.column_stack(
    (np.ones(len(X_train_scaled)), X_train_scaled)
)

X_test_scaled = np.column_stack(
    (np.ones(len(X_test_scaled)), X_test_scaled)
)

# Train linear regression model
weights = np.linalg.lstsq(
    X_train_scaled, y_train, rcond=None
)[0]

# Predict test temperatures
predictions = X_test_scaled @ weights

# Calculate evaluation metrics
mae = np.mean(np.abs(y_test - predictions))
rmse = np.sqrt(np.mean((y_test - predictions) ** 2))

ss_res = np.sum((y_test - predictions) ** 2)
ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)

r2 = 1 - ss_res / ss_tot if ss_tot != 0 else 0

# Save model parameters
model = {
    "features": features,
    "mean": mean.tolist(),
    "std": std.tolist(),
    "weights": weights.tolist()
}

with open("model_parameters.json", "w") as file:
    json.dump(model, file, indent=4)

print("\nAI COOLING OPTIMIZER - MODEL TRAINED!")
print("------------------------------------")
print("Total records:", len(X))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error:", round(mae, 3))
print("Root Mean Squared Error:", round(rmse, 3))
print("R2 Score:", round(r2, 4))
print("\nModel saved as model_parameters.json")
print("Model Performance")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)