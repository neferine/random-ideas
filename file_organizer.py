import os
import shutil

folder_path = '/home/pug/Downloads' #path to folder that you will organize

#Home Directories
home_dir = os.path.expanduser("~")
pic_dir = os.path.join(home_dir,"Pictures")
music_dir = os.path.join(home_dir,"Music")
videos_dir = os.path.join(home_dir,"Videos")
document_dir = os.path.join(home_dir,"Documents")

#file formats
image_formats = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'bmp']
video_formats = ['mp4', 'mov', 'avi' , 'wmv', 'mkv' , 'webm']
music_formats = ['mp3', 'aac' , 'wav', 'flac', 'aiff']
document_formats = [
    'pdf', 'doc', 'docx', 'txt', 'rtf',
    'odt', 'md', 'tex', 'csv', 'xlsx', 'xls',
    'ppt', 'pptx', 'json', 'xml', 'yaml', 'yml'
]

def check_folders(home_dir):
    folders = ["Pictures", "Downloads", "Documents", "Music", "Videos"]

    for folder in folders:
        path = os.path.join(home_dir,folder)
        if not os.path.isdir(path):
            os.makedirs(path)
            print(f"Created missing {path} folder for ya!")
    print("Folders are fine")

check_folders(home_dir)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1][1:].lower()

    try:
        if ext in image_formats:
            shutil.move(file_path , os.path.join(pic_dir, file))
        elif ext in video_formats:
            shutil.move(file_path, os.path.join(videos_dir, file))
        elif ext in music_formats:
            shutil.move(file_path, os.path.join(music_dir, file))
        elif ext in document_formats:            
            shutil.move(file_path, os.path.join(document_dir, file))

    except Exception:
        print("Error moving {file}")

print("File Organization Complete!")
