from tkinter.filedialog import askdirectory
from functions import Number_Of_Files, File_Date
from os import makedirs, path, rmdir, listdir
from shutil import copy2
from datetime import datetime

selected_folder = askdirectory()

select_folder_qty = Number_Of_Files(selected_folder)

final_folder = f"caminho para a pasta final"

for file in listdir(selected_folder):
    file_path = path.join(selected_folder, file) 

    if path.isfile(file_path):
        file_name, extension = path.splitext(file_path)

        if extension.lower() in [".jpg", ".jpeg"]:
            file_date = File_Date(file_path)

            if file_date is not None:
                shoot_date = datetime.strptime(file_date, "Y%:%m:%d %H:%M:%S")
                year = str(shoot_date.year)
                month = str(shoot_date.month).zfill(2)
                day = str(shoot_date.day).zfill(2)
                file_destiny = path.join(final_folder, year, f"Month{month}")

                if not path.exists(file_destiny):
                    makedirs(file_destiny)
                new_file_name = f"Day{day}{extension}"
                new_file_path = path.join(file_destiny, new_file_name)
                copy2(file_path, new_file_path)

            else:
                other_files = path.join(final_folder, "other files")

                if not path.exists(other_files):
                    makedirs(other_files)
                new_file_path = path.join(other_files, file)
                copy2(file_path, new_file_path)

    else:
        other_files = path.join(final_folder, "other files")

        if not path.exists(other_files):
            makedirs(other_files)
        new_file_name = path.join(other_files, file)
        copy2(file_path, new_file_path)
    
final_folder_qty = Number_Of_Files(final_folder)

print(f"The number of files in the final folder is {final_folder_qty}")

if final_folder_qty == select_folder_qty:
    print("All the files have been copied correctly")
else:
    print("Some files couldn't be copied")