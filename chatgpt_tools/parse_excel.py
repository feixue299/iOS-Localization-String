import sys
import os
import openpyxl

# 读取命令行参数
if len(sys.argv) != 2:
    print("请指定Excel文件路径")
    sys.exit(1)

excel_file_path = sys.argv[1]

# 检查文件类型
if not excel_file_path.endswith(".xlsx"):
    print("文件不是一个有效的Excel文件")
    sys.exit(1)

# 打开工作簿并选择第一个工作表
workbook = openpyxl.load_workbook(excel_file_path)
worksheet = workbook.active

# 遍历数据行
for row in worksheet.iter_rows(min_row=2):
    # 获取第一列的值
    key = row[0].value
    if key is None:
        continue

    # 遍历数据列
    for i, cell in enumerate(row[1:], start=2):
        # 获取列头的值
        header = worksheet.cell(row=1, column=i).value
        if header is None:
            continue

        # 获取当前列的值
        value = cell.value
        if value is None:
            continue

        # 写入数据到文件
        output_filename = f"{header}.strings"
        with open(output_filename, "a", encoding="utf-8") as f:
            f.write(f'"{key}" = "{value.strip()}";\n')