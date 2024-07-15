# EPS to PNG Converter

This project converts EPS files to PNG format with transparent backgrounds using Python. It processes all EPS files in the current working directory and saves the converted PNG files in a separate `output` directory.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)
- Ghostscript

## Installation

1. **Install Python**: Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Pillow**: Install the Pillow library using pip:

    ```bash
    pip install Pillow
    ```

3. **Install Ghostscript**:

    - Download and install Ghostscript from the [official website](https://www.ghostscript.com/download/gsdnld.html).
    - Add the Ghostscript `bin` directory to your system's PATH.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

    ```bash
    git clone https://github.com/OCEANOFANYTHINGOFFICIAL/eps-to-png-converter.git
    cd eps-to-png-converter
    ```

2. **Update Ghostscript Path**: Update the `gs_path` variable in the script to point to the Ghostscript `bin` directory on your system.

    ```python
    gs_path = 'path/to/ghostscript/bin'  # Replace with the actual path to gs executable
    ```

3. **Run the Script**: Execute the script to convert all EPS files in the current working directory to PNG with transparent backgrounds.

    ```bash
    python convert_eps_to_png.py
    ```

4. **Check the Output**: The converted PNG files will be saved in the `output` directory.

## Script Explanation

The script performs the following steps:

1. **Define Directories**: Sets the current working directory as the input directory and creates an `output` directory if it doesn't exist.

    ```python
    input_dir = os.getcwd()
    output_dir = os.path.join(input_dir, 'output')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    ```

2. **Update Environment Variable**: Updates the system's PATH environment variable to include the Ghostscript `bin` directory.

    ```python
    os.environ['PATH'] = gs_path + os.pathsep + os.environ['PATH']
    ```

3. **Convert EPS to PNG**: Iterates over all EPS files in the input directory, converts them to PNG with transparent backgrounds, and saves them in the output directory.

    ```python
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.eps'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')
            
            with Image.open(input_path) as img:
                img = img.convert("RGBA")
                datas = img.getdata()

                new_data = []
                for item in datas:
                    if item[0] > 200 and item[1] > 200 and item[2] > 200:
                        new_data.append((255, 255, 255, 0))
                    else:
                        new_data.append(item)
                
                img.putdata(new_data)
                img.save(output_path, 'PNG')
    ```

4. **Completion Message**: Prints a message indicating the completion of the conversion process.

    ```python
    print(f"Conversion complete. All .eps files are converted to .png with transparent backgrounds and saved in '{output_dir}' folder.")
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any improvements or suggestions.

---

Feel free to reach out if you have any questions or need further assistance. Happy converting!
