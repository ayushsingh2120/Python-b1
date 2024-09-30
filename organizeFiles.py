

import os
import shutil

def list_folders(path):
    list_of_files = os.listdir(path)
    print(list_of_files)

def organize_files(address):
    path_of_folder = address

    destination_folder = {
        ".jpg": f"{path_of_folder}/Images",
        ".mkv": f"{path_of_folder}/Videos",
        ".mp4": f"{path_of_folder}/Videos",
        ".mp3": f"{path_of_folder}/Music",
        ".oog": f"{path_of_folder}/Music",
        ".docs": f"{path_of_folder}/Documents",
        ".pdf": f"{path_of_folder}/Documents",
        ".py": f"{path_of_folder}"
    }

    all_files = os.listdir(path_of_folder)


    for file in all_files:
        file_path = os.path.join(path_of_folder,file)

        if(os.path.isfile(file_path)):
            file_ext = os.path.splitext(file)[1].lower()

            if(file_ext == '.py'):
                continue

            if(file_ext in destination_folder):
                destination = destination_folder[file_ext]
            else:

                destination = f"{path_of_folder}/Misc"


            shutil.move(file_path, os.path.join(destination,file))
            print(f"successfully moved {file} at {destination}")

        else:
            print(f"{file} is not a file.")




def create_dir_structure(address):


    add = address 
    
    list_folders(add)

    folders = "Images, Videos, Documents, Music, Misc ".split(",") 
    folders = [folder.strip() for folder in folders] 
    for folder in folders:
        folder_path = os.path.join(add,folder)  
        if(folder in os.listdir(add)):
            print(f"{folder} already present !")
        else:
            print(f"creating folder {folder}")
            os.makedirs(folder_path)
            print(f"folder created at path {folder_path}")

    organize_files(add)

create_dir_structure()









    

 