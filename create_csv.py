import csv
from datetime import datetime
import os

# Target output directory
output_dir = r"C:\Users\hurleysa\Documents\Python\Test Run Github Script"
os.makedirs(output_dir, exist_ok=True)

# Filename and full path
filename = f"sample_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
full_path = os.path.join(output_dir, filename)

# Write CSV
with open(full_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "San Francisco"])

print(f"CSV file saved to {full_path}")
