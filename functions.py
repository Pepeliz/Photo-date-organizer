from os import walk, path, makedirs
from PIL import Image
from pillow_heif import register_heif_opener
from moviepy.editor import VideoFileClip
from PIL.ExifTags import TAGS
from shutil import move

def Number_Of_Files(path_file):
    quantity = 0

    for _, _, files in walk(path_file):
        quantity += len(files)
    
    return quantity


def File_Date(image_path, file_type):
    exif_date = None

    try:
        if file_type.lower() in [".jpg", ".jpeg"]:
            with Image.open(image_path) as image:
                exif_date = image._getexif()

        elif file_type.lower() in [".heif", ".heic"]:
            with Image.open(image_path) as image:
                exif_data = image.info.get('exif', b'')
                if isinstance(exif_data, bytes):
                    exif_data = exif_data.decode('utf-8')
                exif_date = exif_data
                
        elif file_type.lower() in [".mov", ".mp4"]:
            with VideoFileClip(image_path) as video:
                metadata = video.reader.metadata
                if 'creation_time' in metadata:
                    exif_date = metadata['creation_time']

        elif file_type.lower() == ".png":
            with Image.open(image_path) as image:
                exif_data = image.info.get('png', {})
                if 'creation_time' in exif_data:
                    exif_date = exif_data['creation_time']

        if exif_date:
            for tag, value in exif_date.items():
                tag_name = TAGS.get(tag, tag)
                
                if tag_name == 'DateTimeOriginal':
                    return value
                
    except (IOError, AttributeError, Exception) as e:
        print(f"Error processing {image_path}: {e}")

    return None


def Organize_Other_Files(destiny_folder, file_path, file):
    other_files = path.join(destiny_folder, "Other_files")

    if not path.exists(other_files):
        makedirs(other_files)

    new_file_path = path.join(other_files, file)
    move(file_path, new_file_path)