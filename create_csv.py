import csv
from datetime import datetime

# Define some sample data
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "Chicago"]
]

# Filename with timestamp
filename = f"sample_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Write CSV file
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")