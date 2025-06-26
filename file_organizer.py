import os
import shutil

#Set the folder path to the files you want to organize
folder_path = '/home/pug/Downloads' 

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1][1:].lower()

        if ext:
            dest_folder = os.path.join(folder_path, ext.upper())
            os.makedirs(dest_folder, exist_ok=True)
            
            shutil.move(file_path, os.path.join(dest_folder, file))

print("File Organization Complete!")




