# This script is a library for main.py code
# Import necessary libraries
from os import walk, path, makedirs
from shutil import move
import exifread

def number_of_files(path_file):
    '''
    This function counts the number of files in a directory.

    Parameters:
    path_file (str): The path of the directory.

    Returns:
    quantity (int): The number of files in the directory.
    '''
    quantity = 0

    # Walk trough the directory
    for _, _, files in walk(path_file):
        # Count the number of files
        quantity += len(files)
    
    return quantity


def file_date(file_path, file_type):
    '''
    This function retrieves the date of a file from its EXIF data.

    Parameters:
    file_path (str): The path of the file.
    file_type (str): The type of the file ('.jpg', '.jpeg', '.png', '.heic').

    Returns:
    exif_date (str): The date of the file, or None if an error occurs or the date is not found.
    '''
    exif_date = None
    try:
        # Check the file type and read the EXIF data accordingly
        if file_type.lower() in ['.jpg', '.jpeg', '.heic']:
            with open(file_path, 'rb') as image_file:
                tags = exifread.process_file(image_file)
                exif_date = tags.get('EXIF DateTimeOriginal')

        elif file_type.lower() == '.png':
            with open(file_path, 'rb') as image_file:
                tags = exifread.process_file(image_file)
                exif_date = tags.get('Image DateTime')
        
        # If a date was found, convert it to a string
        if exif_date:
            return str(exif_date)

    except (IOError, AttributeError, Exception) as e:
        pass

    return None


def organize_other_files(destiny_folder, file_path, file):
    '''
    This function moves a file to a specified directory.

    Parameters:
    destiny_folder (str): The path of the destination directory.
    file_path (str): The path of the file to be moved.
    file (str): The name of the file to be moved.
    '''
    # Create a new directory for other files if it doesn't exist
    other_files = path.join(destiny_folder, 'Other_files')

    if not path.exists(other_files):
        makedirs(other_files)

    # Move the file to the new directory
    new_file_path = path.join(other_files, file)
    move(file_path, new_file_path)


if __name__ == '__main__':
    print('This script is a library for main.py.')
    print('Please run main.py to execute the main program.')
