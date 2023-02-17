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

# 处理数据并写入文件
def process_data(data, output_file_path):
    # 按第一行的顺序生成文件列表
    header_row = data[0]
    output_files = []
    for i in range(1, len(header_row)):
        if header_row[i] and header_row[i].strip() != "":
            output_files.append(header_row[i])
    
    # 写入文件
    for file_name in output_files:
        file_path = output_file_path + '/' + file_name + '.strings'
        os.makedirs(output_file_path, exist_ok=True)
        with open(file_path, 'w') as f:
            key_group = []
            for row in data[1:]:
                column1, column2 = row[0], row[output_files.index(file_name) + 1]
                if column1 in key_group:
                    continue
                else:
                    key_group.append(column1)
                if column1 is not None and column1.strip() != "" and is_valid_data(column1, column2):
                    line = f'"{column1}" = "{column2.replace("{#}", "%@")}" ;\n'
                    f.write(line)

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
    process_data(data, output_file_path)