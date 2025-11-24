Image Resizer Tool
A lightweight Python utility for batch resizing and format conversion of images using the Pillow library. Designed for developers, designers, and content creators who need fast, reliable preprocessing of image assets.

Features
Batch resize images from any folder

Convert image formats (e.g., PNG to JPEG)

High-quality downscaling using LANCZOS filter

Auto-creates input and output folders

Displays resized images during execution

Easily extensible for CLI, GUI, or web integration

Installation
bash
pip install pillow
Usage
Place your images in the images_input folder.

Run the script:

bash
python image.py
Resized images will appear in the images_output folder.

Configuration
You can customize the following parameters in the script:

python
new_size = (800, 600)         # Target dimensions
output_format = "JPEG"        # Output format
input_folder = "images_input" # Source folder
output_folder = "images_output" # Destination folder
Requirements
Python 3.7 or higher

Pillow (Python Imaging Library fork)

Project Structure
Code
Image-Resizer-Tool/
├── image.py
├── images_input/
└── images_output/
Future Enhancements
Command-line interface with argparse

Aspect ratio preservation

Drag-and-drop GUI using Tkinter or PyQt

Web optimization with WebP support

Logging and error reporting

Integration with Flask for browser-based preview
 Features
Batch processing from any input folder

 Custom resizing with high-quality filters (LANCZOS)

 Format conversion (e.g., PNG → JPEG)

 Auto-creates output folders

 Image preview during execution

 Extensible for CLI, GUI, or web integration

 How to Use
Place images in the images_input folder

Run image.py

Resized images appear in images_output

 Dependencies
Python 3.7+

Pillow (pip install pillow)

 Future Enhancements
CLI support with argparse

Aspect ratio preservation

GUI preview with Tkinter or Flask

WebP optimization for faster web delivery
