import requests
from PIL import Image
from io import BytesIO
import os

# List of part names and corresponding image URLs (you need to manually provide the URLs)
part_names = [
    "Brake Pads", "Oil Filter", "Air Filter", "Radiator", "Timing Belt",
    "Alternator", "Spark Plug", "Battery", "Headlight", "Fuel Pump",
    "Water Pump", "Brake Disc", "Windshield Wiper", "Exhaust Pipe", "Tire"
]

# Example URLs (replace with actual URLs of the images)
part_image_urls = {
    "Brake Pads": "https://img.freepik.com/premium-photo/automotive-brake-pads-isolated-white-background_823268-768.jpg",
    "Oil Filter": "https://img.freepik.com/premium-photo/car-oil-filter-oil-filters-white-background-3d-illustration_943642-5216.jpg",
    "Air Filter": "https://img.freepik.com/free-photo/different-car-accessories-composition_23-2149030384.jpg",
    "Radiator": "https://img.freepik.com/premium-photo/car-radiator-isolated-white-background-3d-render_268321-209.jpg",
    "Timing Belt": "https://img.freepik.com/premium-photo/photo-car-timing-belt_778780-17645.jpg",
    "Alternator": "https://img.freepik.com/premium-photo/car-alternator-isolated-white-background_999671-20445.jpg",
    "Spark Plug": "https://img.freepik.com/premium-photo/spark-plug-cars-with-gasoline-engine-isolated-white-background_322433-2262.jpg",
    "Battery": "https://img.freepik.com/free-vector/car-battery-charger-with-jump-starter-connection-wire-kit-illustration_1284-53950.jpg",
    "Headlight": "https://static.vecteezy.com/system/resources/previews/003/114/935/large_2x/closeup-of-a-headlight-on-a-modern-car-with-reflection-free-photo.JPG",
    "Fuel Pump": "https://img.freepik.com/premium-photo/unit-pumping-liquid-fuel-creating-required-pressure-line-car-fuel-pump-sale-autoanalysis-repair-workshop_136863-5749.jpg",
    "Water Pump": "https://www.shutterstock.com/image-photo/car-water-pump-isolated-on-600nw-1934999780.jpg",
    "Brake Disc": "https://img.freepik.com/premium-photo/3d-rendering-car-brake-disk-brake-disc-dark-background_943642-6565.jpg",
    "Windshield Wiper": "https://img.freepik.com/free-photo/car-wipers-clean-windshields-when-driving-sunny-weather_169016-17984.jpg",
    "Exhaust Pipe": "https://img.freepik.com/premium-photo/close-up-car-s-exhaust-pipe_582637-9042.jpg",
    "Tire": "https://img.freepik.com/free-vector/car-wheel-tires-stacked-top-each-other-realistic-composition-white-background-vector-illustration_1284-82101.jpg?t=st=1721540970~exp=1721544570~hmac=dea1c96ba3fd180e8b5010e173fa1b08ef6836593e4ddaaf90d94c95c5c001db&w=1800"
}

# Directory to save downloaded images
image_dir = "part_images"
os.makedirs(image_dir, exist_ok=True)

# Download images
for part_name, url in part_image_urls.items():
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img_path = os.path.join(image_dir, f"{part_name.replace(' ', '_').lower()}.jpg")
    img.save(img_path)
    print(f"Downloaded {part_name} image.")