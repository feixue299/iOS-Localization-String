import argparse
from parse_strings import parse_file
from parse_excel import *
from find_lproj import get_lproj_folders

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", help="Path to search for lproj folders")
    parser.add_argument("lang_excel_path", help="path to parse excel data")
    parser.add_argument("default_name", default="Localizable", help="string name")
    parser.add_argument('sync_write', default="False", help="sync write to lproj")
    args = parser.parse_args()
    lproj_folders = get_lproj_folders(args.project_path)
    excel_path = args.lang_excel_path
    default_name = args.default_name
    sync_write = args.sync_write

    get_en_info_path = list(filter(lambda x: x.endswith("InfoPlist.strings"), lproj_folders["en"]))

    other_files = []
    if len(get_en_info_path) != 0 :
        en_info_path = get_en_info_path[0]
        en_info_result = list(map(lambda x: list(x.keys())[0], parse_file(en_info_path)))
        other_files = [{"InfoPlist": en_info_result}]

    # 读取 Excel 数据
    data = read_excel_file(excel_path)

    # 处理数据并写入文件
    output_file_path = './output'

    process_data_and_write_file_with_other_files(data, output_file_path, default_name, other_files)
    if sync_write != "False":
        for (key, value) in lproj_folders.items():
            for path in value:
                print(path)
                file_name = os.path.basename(path)
                string_parent_path = output_file_path + "/" + key + "/" + file_name

                file_size = os.path.getsize(string_parent_path)
                if file_size != 0:
                    with open(string_parent_path, 'r') as source_file, open(path, 'w') as target_file:
                    # 读取源文件的内容
                        content = source_file.read()
                        # 把内容写入到目标文件
                        target_file.write(content)