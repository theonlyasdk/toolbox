import os
import cairosvg
import argparse
from tqdm import tqdm

def convert_svg_to_png(input_folder, resolution):
    output_folder = os.path.join(input_folder, f'converted_to_png_{resolution[0]}x{resolution[1]}')
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all SVG files in the input folder
    svg_files = [f for f in os.listdir(input_folder) if f.endswith('.svg')]
    
    # Use tqdm to create a progress bar with a simple format
    for filename in tqdm(svg_files, desc="Converting SVG to PNG", unit="file", bar_format='{l_bar}{bar} [{n_fmt}/{total_fmt}]'):
        svg_file_path = os.path.join(input_folder, filename)
        png_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
        
        # Check if the PNG file already exists
        if os.path.exists(png_file_path):
            continue  # Skip conversion if the PNG file already exists
        
        try:
            # Convert SVG to PNG with specified resolution
            cairosvg.svg2png(url=svg_file_path, write_to=png_file_path, output_width=resolution[0], output_height=resolution[1])
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert SVG files to PNG format with specified resolution.")
    parser.add_argument('input_folder', type=str, help="Path to the folder containing SVG files.")
    parser.add_argument('--resolution', type=int, nargs=2, metavar=('WIDTH', 'HEIGHT'), required=True,
                        help="Resolution to convert the SVGs to, specified as WIDTH HEIGHT.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Convert SVG to PNG
    convert_svg_to_png(args.input_folder, tuple(args.resolution))

if __name__ == "__main__":
    main()
