import pandas as pd
import random
import os
from PIL import Image, ImageDraw, ImageFont
dd	dd
# Sample data
years = list(range(1999, 2025))
makes = ['Honda', 'Toyota', 'BMW', 'Mercedes Benz', 'Ford', 'Chevrolet', 'Nissan', 'Volkswagen', 'Audi', 'Hyundai', 'Kia', 'Mazda', 'Subaru', 'Lexus', 'Jaguar']
part_names = ['Air Filter', 'Oil Filter', 'Brake Pads', 'Spark Plug', 'Battery', 'Alternator', 'Headlight', 'Radiator', 'Timing Belt', 'Fuel Pump', 'Water Pump', 'Brake Disc', 'Windshield Wiper', 'Exhaust Pipe', 'Tire']

def generate_image(year, make, part_name, output_dir="images"):
    """Generate an image with the part name."""
    img = Image.new('RGB', (200, 50), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text = f"{year} {make} {part_name}"
    d.text((10, 10), text, font=font, fill=(0, 0, 0))
    image_name = f"{year}_{make.replace(' ', '_')}_{part_name.replace(' ', '_')}.png"
    image_path = os.path.join(output_dir, image_name)
    img.save(image_path)
    return image_path

def generate_csv(file_path):
    """Generate CSV file with year, make, part name, and part name image."""
    data = {
        'year': [],
        'make': [],
        'part_name': [],
        'part_image': []
    }

    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    for year in years:
        for make in makes:
            for part_name in part_names:
                part_name_image = generate_image(year, make, part_name, output_dir)

                data['year'].append(year)
                data['make'].append(make)
                data['part_name'].append(part_name)
                data['part_image'].append(part_name_image)

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"CSV file '{file_path}' generated successfully!")

# Generate the CSV file
csv_file_path = 'car_parts_with_images.csv'
generate_csv(csv_file_path)
