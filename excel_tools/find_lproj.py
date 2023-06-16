import os

def get_lproj_folders(path):
    lproj_folders = {}
    for root, dirs, files in os.walk(path):
        for folder in dirs:
            if folder.endswith(".lproj"):
                folder_path = os.path.join(root, folder)
                folder_name = os.path.splitext(folder)[0]
                if folder_name not in lproj_folders:
                    lproj_folders[folder_name] = []
                for file in os.listdir(folder_path):
                    if file.endswith(".strings"):
                        lproj_folders[folder_name].append(os.path.join(folder_path, file))
    return lproj_folders