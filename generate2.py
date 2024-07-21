import pandas as pd
import random
import os
from PIL import Image, ImageDraw, ImageFont
# Sample data
years = list(range(1999, 2025))
makes = ['Honda', 'Toyota', 'BMW', 'Mercedes Benz', 'Ford', 'Chevrolet', 'Nissan', 'Volkswagen', 'Audi', 'Hyundai', 'Kia', 'Mazda', 'Subaru', 'Lexus', 'Jaguar']
part_names = ['Air Filter', 'Oil Filter', 'Brake Pads', 'Spark Plug', 'Battery', 'Alternator', 'Headlight', 'Radiator', 'Timing Belt', 'Fuel Pump', 'Water Pump', 'Brake Disc', 'Windshield Wiper', 'Exhaust Pipe', 'Tire']


def generate_image(display_text, part_name):
    # Define the image size
    image_size = (500, 500)

    # Generate a random color for the background
    #background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    background_color = (255, 255, 255)

    # Create a new image with the background color
    image = Image.new('RGB', image_size, background_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 30)  # You can specify the font path here
    except IOError:
        font = ImageFont.load_default()

    # Define the text and its size
    text = display_text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_size = (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1])


    # Calculate the position for the text to be centered
    #text_position = ((image_size[0] - text_size[0]) / 2, (image_size[1] - text_size[1]) / 2 - 100)
    text_position = ((image_size[0] - text_size[0]) / 2, 20)  # Adjust vertical position as needed

    # Add text to image
    text_color = (0, 0, 0)  # Black text
    draw.text(text_position, text, fill=text_color, font=font)

    # Add the part image if available
    img_path = os.path.join("part_images", f"{part_name.replace(' ', '_').lower()}.jpg")
    if os.path.exists(img_path):
        part_image = Image.open(img_path)
        # Calculate new size to maintain aspect ratio and cover 80% of the image size
        max_dimension = int(0.9 * min(image_size))
        part_image.thumbnail((max_dimension, max_dimension), Image.LANCZOS)

        # Calculate position to center the part image
        part_image_position = (
            (image_size[0] - part_image.size[0]) // 2,
            (image_size[1] - part_image.size[1]) // 2 + 40
        )
        image.paste(part_image, part_image_position)

    # Directory to save generated images
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    # Save or display the image
    output_path = os.path.join(output_dir, f"{display_text.replace(' ', '_').lower()}.png")
    image.save(output_path)
    #print(f"Generated image for {display_text} saved at {output_path}")
    return image


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
                part_name_image = generate_image(str(year) +" "+ make +" "+ part_name, part_name)

                #print(f"year={year}, make={make}, part_name={part_name}")

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
