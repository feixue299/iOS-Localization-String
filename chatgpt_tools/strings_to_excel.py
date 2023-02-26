import argparse
from find_lproj import get_lproj_folders
import os
import pandas as pd
from parse_strings import parse_file

# 排序语言
def sortLang(langData):
    sort_lang = ["en", "zh-Hans", "es", "it", "fr", "de", "nl", "sv", "pl", "pt-PT", "ru"]
    sort_lang.reverse()
    for lang in sort_lang:
        advance(lang, langData)

# 将lang提前
def advance(lang, langData):
    for index in range(len(langData)):
        value = langData[index]
        if value[0] == lang:
            langData.remove(value)
            langData.insert(0, value)
            break
        

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
        excel_data = {}
        
        lang_data = list(value.items())
        sortLang(lang_data)

        if len(lang_data) > 0:
            first_lang = lang_data[0]
            
            first_column = parse_file(first_lang[1])
            
            excel_data["ios-id"] = []
            excel_data[first_lang[0]] = []

            for dic in first_column:
                key = list(dic.keys())[0]
                excel_data["ios-id"].append(key)
                excel_data[first_lang[0]].append(dic[key])

        else:
            continue

        df = pd.DataFrame(excel_data)
        parent_path = './output/'
        os.makedirs(parent_path, exist_ok=True)
        df.to_excel(parent_path + excel_name + ".xlsx", index=False)
    
