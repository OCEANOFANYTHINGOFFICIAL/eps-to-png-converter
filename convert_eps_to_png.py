import os
from PIL import Image

# Define the input and output directories
input_dir = os.getcwd()
output_dir = os.path.join(input_dir, 'output')

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the Ghostscript path explicitly
gs_path = 'path//to//ghostscript//bin'  # Replace with the actual path to gs executable

# Update the environment variable for Ghostscript
os.environ['PATH'] = gs_path + os.pathsep + os.environ['PATH']

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.eps'):
        # Define the full path to the input and output files
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')
        
        # Open the EPS file and convert it to PNG with transparent background
        with Image.open(input_path) as img:
            img = img.convert("RGBA")  # Convert image to RGBA to add alpha channel
            datas = img.getdata()

            new_data = []
            for item in datas:
                # Change all white (also shades of whites)
                # to transparent
                if item[0] > 200 and item[1] > 200 and item[2] > 200:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            
            img.putdata(new_data)
            img.save(output_path, 'PNG')

print(f"Conversion complete. All .eps files are converted to .png with transparent backgrounds and saved in '{output_dir}' folder.")
