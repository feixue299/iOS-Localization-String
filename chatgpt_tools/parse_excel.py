import sys
import openpyxl
import pathlib
import os

# 检查路径是否为Excel文件
def is_excel_file(file_path):
    return file_path.endswith('.xlsx') or file_path.endswith('.xls')

# 读取Excel文件并返回二维数组
def read_excel_file(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    return data

# 检查两个列的数据是否都不为空
def is_valid_data(column1, column2):
    return column1 is not None and column2 is not None


# 返回数据组，[{lang: [{key: value}]}]
def process_data(data):
    # 按第一行的顺序生成文件列表
    header_row = data[0]
    langsDic = []
    for i in range(1, len(header_row)):
        if header_row[i]:
            langsDic.append({header_row[i]: []})
    
    langs = []
    for langDic in langsDic:
        langs.append(list(langDic.keys())[0])

    for langDic in langsDic:
        lang = list(langDic.keys())[0]
        if lang.strip() == "":
            continue
        key_group = []
        for row in data[1:]:
            column1, column2 = row[0], row[langs.index(lang) + 1]

            if column1 in key_group:
                continue
            else:
                key_group.append(column1)

            if column1 is not None and column1.strip() != "" and is_valid_data(column1, column2):
                dic = {column1: column2.replace("{#}", "%@")}
                langDic[lang].append(dic)
    return langsDic
        

# 处理数据并写入文件
def process_data_and_write_file(data, output_file_path):
    process_data_and_write_file_with_other_files(data, output_file_path, [])
                    

def process_data_and_write_file_with_other_files(data, output_file_path, other_files):
    result = process_data(data)
    # 写入文件
    for langdic in result:
        file_name = list(langdic.keys())[0]
        file_path = output_file_path + '/' + file_name + '.strings'
        os.makedirs(output_file_path, exist_ok=True)

        other_open_files = []
        for file in other_files:
            other_file_name = list(file.keys())[0]
            other_file_path = output_file_path + '/' + other_file_name + '.strings'
            other_files.append(open(other_file_path, 'w'))

        with open(file_path, 'w') as f:
            for lang_data in langdic[file_name]:
                column1 = list(lang_data.keys())[0]
                column2 = lang_data[column1]
                line = f'"{column1}" = "{column2}" ;\n'

                has_writed = False
                for index in range(len(other_files)):
                    file = other_files[index]
                    key = list(file.keys())[0]
                    if column1 in file[key]:
                        other_files[index].write(line)
                        has_writed = True
                        break

                if not has_writed:
                    f.write(line)
        
        for file in other_open_files:
            file.close()

# 程序入口
if __name__ == '__main__':
    # 读取命令行参数
    file_path = sys.argv[1]

    # 检查文件类型
    if not is_excel_file(file_path):
        print(f'{file_path} 不是一个有效的 Excel 文件路径')
        sys.exit()

    # 读取 Excel 数据
    data = read_excel_file(file_path)

    # 处理数据并写入文件
    output_file_path = './output'
    process_data_and_write_file(data, output_file_path)