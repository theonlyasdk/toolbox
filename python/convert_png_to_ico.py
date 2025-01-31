import os
import sys
from PIL import Image
from tqdm import tqdm

def convert_png_to_ico(png_file, output_dir):
    try:
        # Open the PNG file
        with Image.open(png_file) as img:
            # Convert to ICO and save
            ico_file = os.path.join(output_dir, os.path.splitext(os.path.basename(png_file))[0] + '.ico')
            img.save(ico_file, format='ICO')
            print(f"Converted: {png_file} to {ico_file}")
    except Exception as e:
        print(f"Error converting {png_file}: {e}")

def convert_folder_to_ico(folder_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    
    if not png_files:
        print("No PNG files found in the specified folder.")
        return

    print(f"Converting {len(png_files)} PNG files to ICO format...")
    
    for png_file in tqdm(png_files, desc="Converting files"):
        convert_png_to_ico(os.path.join(folder_path, png_file), output_dir)

    print(f"All files converted. ICO files are saved in: {output_dir}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert_png_to_ico.py <input_file_or_folder> <output_directory>")
        print("Example: python convert_png_to_ico.py image.png output_folder")
        print("Example: python convert_png_to_ico.py folder_with_pngs output_folder")
        sys.exit(1)

    input_path = sys.argv[1]
    output_directory = sys.argv[2]

    if os.path.isfile(input_path):
        convert_png_to_ico(input_path, output_directory)
    elif os.path.isdir(input_path):
        convert_folder_to_ico(input_path, output_directory)
    else:
        print("Error: The specified input path is neither a file nor a directory.")
        sys.exit(1)

if __name__ == "__main__":
    main()
