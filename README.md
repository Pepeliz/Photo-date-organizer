# Photo date organizer

This script is intended to organize photos in a directory based on the date their were shooted using the EXIF data of the image. It has support to JPEG, JPG, HEIC and PNG files. The files that doesn't have date or are not supported by the script will be moved to other folder called "Other Files". It's important to know that the script will rename the files that have date  and will move every single file in the folder that you selected. This is my first project, feel free to point out areas for improvement and suggest ways to enhance the code.


## Prerequisites

This code was made in python 3.11.5, make sure that you have ExifRead installed in your machine, the version used is 2.3.2. You can install ExifRead using the following command:

```bash
pip install ExifRead == 2.3.2
```
