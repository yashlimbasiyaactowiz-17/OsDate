import os
source_path = r"C:/Users/yash.limbasiya/Desktop/date"
destination_path = r"C:/Users/yash.limbasiya/Desktop/2027_Date_folders/"

def move_file(src_path,dst_path):

    for folder in os.listdir(src_path):# folder
        # if folder == '2026-02-22':
        src_folder_path = os.path.join(src_path,folder)
        year_change = folder.replace("2026", "2027")
        dest_folder=os.path.join(dst_path,year_change)

        for src_folder_file in os.listdir(src_folder_path):# files
            src_file_path = os.path.join(src_folder_path,src_folder_file)
            dest_file_path=os.path.join(dest_folder,src_folder_file)
            os.rename(src_file_path,dest_file_path)
def remove_file(dest_path):
    for folder in os.listdir(dest_path):
        folder_path = os.path.join(dest_path,folder)
        for src_folder_file in os.listdir(folder_path):
            src_file_path = os.path.join(folder_path,src_folder_file)
            if src_folder_file.endswith(".py") or src_folder_file.endswith(".java"):
                os.remove(src_file_path)
move_file(source_path,destination_path)
remove_file(destination_path)# main destination path