import csv
import os
from collections import defaultdict

MAP_FOLDER = "map_outputs"
RESULTS_FOLDER = "results"

os.makedirs(RESULTS_FOLDER, exist_ok=True)

counts = defaultdict(int)

# Read each map output file
for filename in os.listdir(MAP_FOLDER):
    if filename.startswith("map_") and filename.endswith(".csv"):
        with open(os.path.join(MAP_FOLDER, filename), newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                counts[row["item_category"]] += int(row["count"])

# Write final aggregated results
output_path = os.path.join(RESULTS_FOLDER, "final_counts.csv")

with open(output_path, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["item_category", "total_count"])
    for key, value in counts.items():
        writer.writerow([key, value])

print("✅ Reduce step complete. Check results/final_counts.csv")
