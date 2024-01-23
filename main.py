from tkinter import Tk
from tkinter.filedialog import askdirectory
from functions import Number_Of_Files, File_Date, Organize_Other_Files
from os import makedirs, path, walk
from shutil import move
from datetime import datetime

Tk().withdraw()
selected_folder = askdirectory()

select_folder_qty = Number_Of_Files(selected_folder)
print(f"The number of files in the folder that you selected is {final_folder_qty}")

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
            _, extension = path.splitext(file_path)

            if extension.lower() in [".jpg", ".jpeg", ".heic", ".heif", ".mov", ".mp4", ".png"]:
                date = File_Date(file_path, extension)

                if date is not None:
                    shoot_date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")

                    date_string = shoot_date.strftime("%Y_%m_%d")
                    year, month, day = date_string.split("_")

                    time_string = shoot_date.strftime("%H_%M_%S")

                    file_destiny = path.join(final_folder, year, f"Month_{month}")

                    if not path.exists(file_destiny):
                        makedirs(file_destiny)

                    new_file_name = f"Day_{day}_{time_string}{extension}"
                    new_file_path = path.join(file_destiny, new_file_name)
                    move(file_path, new_file_path)

                else:
                    Organize_Other_Files(final_folder, file_path, file)

            else:
                Organize_Other_Files(final_folder, file_path, file)
                
other_files_qty = Number_Of_Files(path.join(final_folder, "Other_files"))

final_folder_qty = Number_Of_Files(final_folder) - other_files_qty

print(f"The number of files organized is {final_folder_qty}")

if final_folder_qty == select_folder_qty:
    print("All the files have been copied correctly")

else:
    print(f"The number of files without date is {other_files_qty}")
