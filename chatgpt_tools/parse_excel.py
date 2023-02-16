import sys
import os
import openpyxl

# 获取命令行输入的路径
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print("请提供需要检查的Excel文件路径")
    sys.exit()

# 检查文件是否存在
if not os.path.isfile(path):
    print("指定路径不是一个有效的文件路径")
    sys.exit()

# 检查文件是否为Excel文件
if not path.endswith(".xlsx"):
    print("指定文件不是一个Excel文件")
    sys.exit()

# 解析Excel文件
workbook = openpyxl.load_workbook(path)
sheet = workbook.active
rows = []
for row in sheet.iter_rows():
    row_data = []
    for cell in row:
        row_data.append(cell.value)
    rows.append(row_data)

# 生成文件
header = rows[0][1:]  # 第一行的数据
for i in range(1, len(rows[0])):
    if not header[i-1] or all(row[i] is None for row in rows[1:]):  # 不包含值为空的列
        continue
    file_data = []
    for j in range(1, len(rows)):
        if rows[j][i] is None:  # 不包含值为空的行
            continue
        data = f'"{rows[j][0]}" = "{rows[j][i]}" ;'
        file_data.append(data)
    if not file_data:
        continue
    file_name = f"{header[i-1]}.strings"
    with open(file_name, "w") as f:
        f.write('\n'.join(file_data))
    print(f"{file_name} 生成成功")