# Photo date organizer

This script organize photos in a directory based on the date their were shooted using the EXIF data of the image. It has support to JPEG, JPG, HEIC and PNG files. The files that doesn't have date or are not supported by the script will be moved to other folder called "Other Files". It's important to know that the script will rename the files that have date  and will move every single file in the folder that you selected. 

## Project purpose

This is my first project and is intended to demonstrate my python knowledge, feel free to suggest ways to improve the script.

## Prerequisites

This code was made in python 3.11.5, make sure that you have ExifRead installed in your machine, the version used is 2.3.2. You can install ExifRead using the following command:

```bash
pip install ExifRead==2.3.2
```

## How to run the code

1. Clone the repository

```bash
git clone https://github.com/Pepeliz/Photo-date-organizer.git
```

2. Navigate to the project directory:

```bash
cd Photo-date-organizer
```

3. Run the script:

```bash
python main.py
```

## Project Structure

- `main.py` Contains the main implementation of the code.
- `functions.py` Contains the implementation of various functions.
