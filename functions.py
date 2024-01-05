from os import walk, path
from PIL import Image
from PIL.ExifTags import TAGS
from shutil import move


def Number_Of_Files(path_file):
    quantity = 0 
    for path, subfolder, files in walk(path_file):
        for name in files:
            quantity += 1
    return quantity 


def File_Date(image_path):
    try:
        with Image.open(image_path) as image:
            exif_date = image._getexif()
            if exif_date:
                for tag, value in exif_date.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == 'DateTimeOriginal':
                        return value
    except (IOError, AttributeError):
        pass
    return None