
import csv
import random
from pathlib import Path

random.seed(42)

# Generate 2000 simulated server records
records = []

for i in range(2000):

    cpu_usage = random.uniform(10, 100)
    ambient_temp = random.uniform(18, 38)
    airflow = random.uniform(1.5, 5.0)
    cooling_power = random.uniform(2, 15)

    inlet_temp = (
        ambient_temp
        + 0.25 * (100 - airflow * 20)
        + random.gauss(0, 0.8)
    )

    server_temp = (
        inlet_temp
        + 0.12 * cpu_usage
        - 0.65 * airflow
        - 0.25 * cooling_power
        + random.gauss(0, 1.0)
    )

    records.append({
        "cpu_usage": round(cpu_usage, 2),
        "ambient_temp": round(ambient_temp, 2),
        "inlet_temp": round(inlet_temp, 2),
        "airflow": round(airflow, 2),
        "cooling_power": round(cooling_power, 2),
        "server_temp": round(server_temp, 2)
    })

# Save the dataset
output_path = Path(__file__).resolve().parent / "server_data.csv"

with open(output_path, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=records[0].keys()
    )
    writer.writeheader()
    writer.writerows(records)

print("Dataset created successfully!")
print("Total records:", len(records))
print("Dataset location:", output_path)

print("\nFirst 5 records:")
for record in records[:5]:
    print(record)

print("\nDataset generation completed!")
