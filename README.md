# PNG Finder

A Python script to search a folder (and all subfolders) for **PNG files**, even if:

* The file doesn’t have a `.png` extension
* Metadata is missing or incorrect

The script checks the **binary signature** of each file to verify whether it’s a real PNG, then outputs the full file paths to a `.txt` file.

---

## Features

* **Recursive search** through all subdirectories
* **Extension-independent detection** using the PNG magic number (`\x89PNG\r\n\x1a\n`)
* **Simple output** to a text file for easy review
* Works on **Windows**, **macOS**, and **Linux** (Python 3+)

---

## Installation

1. Download the file.

2. Make sure Python 3 is installed:
   python --version

3. python findpngs.py
   

---

## Usage

1. Run the script in the terminal:
   python findpngs.py

2. Enter the folder path you want to search when prompted.

3. Optionally enter an output filename (default: pngfiles.txt).

Example:
Enter the folder path to search: C:\Users\User\AppData\Roaming\.minecraft\assets\objects
Enter output text file name (default: pngfiles.txt):
Search complete. Found 42 PNG files.
Results saved to: C:\path\to\png\_files.txt

---

## Output Example

C:\Users\Example\Pictures\image1
C:\Users\Example\Pictures\holiday\_photo
D:\Backups\old\_image.png

---

## How It Works

* The script reads the **first 8 bytes** of each file.
* If the file header matches the PNG signature (`\x89PNG\r\n\x1a\n`), it’s considered a PNG.
* No reliance on file extension or metadata.

---

## Author

Made by **`._rayzz`** 

---

## License

This project is licensed under the MIT License – feel free to use, modify, and share.
