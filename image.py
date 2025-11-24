import os
from PIL import Image

input_folder = "images_input"
output_folder = "images_output"

# Create folders if they don't exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Desired size (width, height)
new_size = (800, 600)

# Desired format (e.g., "JPEG", "PNG")
output_format = "JPEG"

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Resize with high-quality filter
            resized_img = img.resize(new_size, Image.LANCZOS)
            resized_img.show()
            # Build output path (change extension if converting)
            base_name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            # Save in desired format
            resized_img.save(output_path, output_format)

print("Batch resize and conversion complete!")
