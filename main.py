# Import necessary libraries
from tkinter import Tk, Button, Label, filedialog, Text, END
from functions import number_of_files, file_date, organize_other_files
from os import makedirs, path, walk
from shutil import move
from datetime import datetime
from time import sleep

def select_folder(label_widget):
    '''
    Function to open a dialog box to select a directory and update a label widget with the selected directory.

    Parameters:
    label_widget (tkinter.Label): The label widget to be updated with the selected directory.

    Returns:
    str: The path of the selected directory.
    '''
    selected_folder = filedialog.askdirectory()
    label_widget.config(text=f'Folder: {selected_folder}')
    return selected_folder


def main():
    '''
    Main function to organize files in a directory based on their creation date.
    '''
    # Clean text
    text_widget.delete(1.0, END)

    # Get the selected folder from the label widget
    selected_folder = label_source.cget('text').replace('Folder: ', '')
    final_folder = label_destination.cget('text').replace('Folder: ', '')

    # Check if a folder was selected
    if not selected_folder:
        text_widget.insert(END, 'No folder was selected. Please select a folder.\n')
        sleep(1)
        return

    # Count the number of files in the selected directory
    num_files = number_of_files(selected_folder)
    text_widget.insert(END, f'The folder you selected has {num_files} files.\n')
    sleep(0.5)

    # Check if the folder is empty
    if num_files == 0:
        text_widget.insert(END, 'The selected folder is empty. Please select a valid folder.\n')
        sleep(1)
        return

    # Iterate through the selected directory using walk
    for root, _, files in walk(selected_folder):
        # Process each file
        for file in files:
            file_path = path.join(root, file)
            _, extension = path.splitext(file_path)

            # Check the file extension
            if extension.lower() in ['.jpg', '.jpeg', '.heic', '.heif', '.png']:
                date = file_date(file_path, extension)

                # If the file has a date, organize it by date
                if date is not None:
                    organize_by_date(final_folder, file_path, file, date, extension)
                # If the file doesn't have a date, move it to the 'Other_files' folder
                else:
                    organize_other_files(final_folder, file_path, file)
            # If the file has an unsupported extension, move it to the 'Other_files' folder
            else:
                organize_other_files(final_folder, file_path, file)

    # Count the number of files in the 'Other_files' folder and the final folder
    other_files_qty = number_of_files(path.join(final_folder, 'Other_files'))
    final_folder_qty = number_of_files(final_folder) - other_files_qty

    # Print the number of organized files
    text_widget.insert(END, f'The number of files organized is {final_folder_qty}.\n')
    sleep(0.5)

    # Check if all files have been copied correctly
    if final_folder_qty == number_of_files(selected_folder):
        text_widget.insert(END, 'All the files have been copied correctly.\n')
    else:
        text_widget.insert(END, f'The number of files without date is {other_files_qty}.\n')


def organize_by_date(final_folder, file_path, file, date, extension):
    '''
    Organize a file by its creation date.

    Parameters:
    final_folder (str): The path of the final folder.
    file_path (str): The path of the file to be organized.
    file (str): The name of the file to be organized.
    date (str): The creation date of the file.
    extension (str): The extension of the file.
    '''
    # Parse the date
    shoot_date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')

    # Format the date and time
    year, month, day = shoot_date.strftime('%Y_%m_%d').split('_')
    hour, minute, second = shoot_date.strftime('%H_%M_%S').split('_')

    # Create the destination directory
    file_destiny = path.join(final_folder, year, f'{datetime.strptime(month, "%m").strftime("%B")}')

    # Create the destination directory if it doesn't exist
    if not path.exists(file_destiny):
        makedirs(file_destiny)

    # Move the file to the destination directory
    new_file_name = f'Day_{day}_{hour}h_{minute}min_{second}sec{extension}'
    new_file_path = path.join(file_destiny, new_file_name)
    move(file_path, new_file_path)

# Run the main function
if __name__ == '__main__':
    root = Tk()
    root.title('Photo Organizer')
    root.geometry('500x300')

    label_source = Label(root, text='Source Folder: ')
    label_source.pack(pady=10)
    btn_select_source = Button(root, text='Select Source Folder', command=lambda: select_folder(label_source))
    btn_select_source.pack(pady=10)

    label_destination = Label(root, text='Destination Folder: ')
    label_destination.pack(pady=10)
    btn_select_destination = Button(root, text='Select Destination Folder', command=lambda: select_folder(label_destination))
    btn_select_destination.pack(pady=10)

    btn_execute = Button(root, text='Execute', command=main)
    btn_execute.pack(pady=10)
    
    text_widget = Text(root)
    text_widget.pack(pady=10)

    # Start the main GUI loop
    root.mainloop()