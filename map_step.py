import csv
import os

DATA_FOLDER = "data"
OUTPUT_FOLDER = "map_outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each partition file independently (like separate workers)
for filename in os.listdir(DATA_FOLDER):
    if filename.startswith("partition") and filename.endswith(".csv"):
        input_path = os.path.join(DATA_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"map_{filename}")

        with open(input_path, newline="", encoding="utf-8") as infile, \
             open(output_path, "w", newline="", encoding="utf-8") as outfile:

            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)

            # map output header
            writer.writerow(["item_category", "count"])

            # emit (key, value) pairs like: (laptop, 1)
            for row in reader:
                writer.writerow([row["item_category"], 1])

print("✅ Map step complete. Check the map_outputs/ folder.")
