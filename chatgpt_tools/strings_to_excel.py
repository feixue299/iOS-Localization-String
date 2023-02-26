import argparse
from find_lproj import get_lproj_folders
import os
import pandas as pd


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", help="Path to search for lproj folders")
    args = parser.parse_args()
    lproj_folders = get_lproj_folders(args.project_path)
    langs_data = {}
    for key, value in lproj_folders.items():
        for path in value:
            file_name = os.path.basename(path)

            if file_name is None:
                continue

            if file_name not in langs_data:
                langs_data[file_name] = {}
            
            langs_data[file_name][key] = path

    
    for key, value in langs_data.items():
        excel_name, extension = os.path.splitext(key)

        for k, v in value.items():
            print(k, ":", v)
    
