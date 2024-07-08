import csv
import random

# Define the years, makes, and part names
years = list(range(2000, 2024 + 1))
makes = ["Honda", "Toyota", "BMW", "Mercedes-Benz", "Ford", "Chevrolet", "Nissan", "Hyundai", "Kia", "Volkswagen", "Audi", "Mazda", "Subaru", "Lexus", "Volvo", "Porsche", "Jaguar", "Fiat", "Peugeot"]
part_names = ["Air Filter", "Oil Filter", "Brake Pad", "Spark Plug", "Battery", "Fuel Pump", "Radiator", "Alternator", "Headlight", "Taillight", "Exhaust", "Transmission", "Clutch", "Water Pump", "Timing Belt", "Shock Absorber", "Muffler", "Windshield Wiper", "Coolant Hose"]

# Generate data
data = []
for year in years:
    for make in makes:
        for part_name in part_names:
            data.append([year, make, part_name])

# Shuffle the data to randomize
random.shuffle(data)

# Define the CSV file name
csv_file_name = "car_parts.csv"

# Write to CSV file
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["year", "make", "part_name"])  # Write the header
    writer.writerows(data)  # Write the data

print(f"CSV file '{csv_file_name}' generated successfully.")