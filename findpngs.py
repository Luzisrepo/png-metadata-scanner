import os

def is_png(file_path):
    """Check if file is a PNG by reading the first 8 bytes (PNG magic number)."""
    try:
        with open(file_path, 'rb') as f:
            header = f.read(8)
            # PNG signature: 89 50 4E 47 0D 0A 1A 0A
            return header == b'\x89PNG\r\n\x1a\n'
    except (OSError, PermissionError):
        return False

def find_pngs(start_dir, output_file="png_files.txt"):
    """Search a folder recursively for PNG files and save results to a text file."""
    png_files = []

    for root, _, files in os.walk(start_dir):
        for name in files:
            file_path = os.path.join(root, name)
            if is_png(file_path):
                png_files.append(os.path.abspath(file_path))

    # Write results to output file
    with open(output_file, 'w', encoding='utf-8') as out:
        for path in png_files:
            out.write(path + '\n')

    print(f"Search complete. Found {len(png_files)} PNG files.")
    print(f"Results saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    folder_to_search = input("Enter the folder path to search: ").strip('"')
    output_filename = input("Enter output text file name (default: png_files.txt): ").strip()
    if not output_filename:
        output_filename = "png_files.txt"

    find_pngs(folder_to_search, output_filename)
