import os
import sys
from PIL import Image
from tqdm import tqdm
from datetime import datetime

def resize_image(input_path, output_path, size, create_new_file):
    """Resize an image to the specified size."""
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)  # Use LANCZOS for high-quality resizing
        
        # If create_new_file is True, modify the output filename
        if create_new_file:
            base, ext = os.path.splitext(output_path)
            output_path = f"{base}_{size[0]}x{size[1]}{ext}"
        
        img.save(output_path)
        return output_path

def resize_images_in_folder(input_folder, output_folder, size, create_new_file):
    """Resize all images in the input folder and save them to the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    modified_files = []
    for filename in tqdm(os.listdir(input_folder), desc="Resizing images"):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            modified_files.append(resize_image(input_path, output_path, size, create_new_file))

    return modified_files

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Resize images to a specified size.")
    parser.add_argument('-i', '--input', type=str, help='Path to the input image or folder', required=True)
    parser.add_argument('-o', '--output', type=str, help='Path to the output folder', required=True)
    parser.add_argument('-s', '--size', type=int, nargs=2, help='New size as width height', required=True)
    parser.add_argument('--new', action='store_false', help='Create new files instead of overwriting')

    args = parser.parse_args()

    size = tuple(args.size)

    if os.path.isdir(args.input):
        # Resize images in a folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_folder = os.path.join(args.output, f'images_resized_{timestamp}')
        modified_files = resize_images_in_folder(args.input, output_folder, size, args.new)
        print("Modified files:")
        for file in modified_files:
            print(file)
    elif os.path.isfile(args.input):
        # Resize a single image
        output_path = os.path.join(args.output, os.path.basename(args.input))
        modified_file = resize_image(args.input, output_path, size, args.new)
        print(f"Modified file: {modified_file}")
    else:
        print("Input path is neither a file nor a directory.")
        sys.exit(1)

if __name__ == "__main__":
    main()
