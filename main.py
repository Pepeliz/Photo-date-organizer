from tkinter import Tk
from tkinter.filedialog import askdirectory
from functions import Number_Of_Files, File_Date
from os import makedirs, path, rmdir, walk
from shutil import move
from datetime import datetime

Tk().withdraw()
selected_folder = askdirectory()

select_folder_qty = Number_Of_Files(selected_folder)

parent_folder = path.dirname(selected_folder)

final_folder_name = f"{path.basename(selected_folder)}_organized"

final_folder = path.join(parent_folder, final_folder_name)

if not path.exists(final_folder):
    makedirs(final_folder)

else:
    print(f"The folder '{final_folder}' already exists.")

for root, _, files in walk(selected_folder):
    for file in files:
        file_path = path.join(root, file)

        if path.isfile(file_path):
            _ , extension = path.splitext(file_path)

            if extension.lower() in [".jpg", ".jpeg"]:
                image_date = File_Date(file_path)

                if image_date is not None:
                    shoot_date = datetime.strptime(image_date, "%Y:%m:%d %H:%M:%S")
                    year = str(shoot_date.year)
                    month = str(shoot_date.month).zfill(2)
                    day = str(shoot_date.day).zfill(2)
                    file_destiny = path.join(final_folder, year, f"Month_{month}")

                    if not path.exists(file_destiny):
                        makedirs(file_destiny)
                    new_file_name = f"Day_{day}{extension}"
                    new_file_path = path.join(file_destiny, new_file_name)
                    move(file_path, new_file_path)

                else:
                    other_files = path.join(final_folder, "Other_files")

                    if not path.exists(other_files):
                        makedirs(other_files)
                    new_file_path = path.join(other_files, file)
                    move(file_path, new_file_path)

            else:
                other_files = path.join(final_folder, "Other_files")

                if not path.exists(other_files):
                    makedirs(other_files)
                new_file_path = path.join(other_files, file)
                move(file_path, new_file_path)

final_folder_qty = Number_Of_Files(final_folder)

print(f"The number of files organized is {final_folder_qty}")

if final_folder_qty == select_folder_qty:
    print("All the files have been copied correctly")
else:
    print(f"The number of files without date is {Number_Of_Files(other_files)}")