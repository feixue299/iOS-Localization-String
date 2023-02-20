import os
import argparse
from parse_strings import parse_file 

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", help="Path to search for lproj folders")
    parser.add_argument("lang_excel_path", help="path to parse excel data")
    args = parser.parse_args()
    lproj_folders = get_lproj_folders(args.project_path)

    en_info_path = list(filter(lambda x: x.endswith("InfoPlist.strings"), lproj_folders["en"]))[0]
    en_info_result = list(map(lambda x: list(x.keys())[0], parse_file(en_info_path)))
    print("en_info_result:", en_info_result)