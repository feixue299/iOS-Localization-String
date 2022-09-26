# 当我们拿到一个项目时，首先要在项目运行环境安装 requirement.txt 所包含的依赖：
# pip install -r requirement.txt
# 当我们要把环境中的依赖写入 requirement.txt 中时，可以借助 freeze 命令：
# pip freeze >requirements.txt

import sys
from generate import generateExcel
from merge import mergeExcelToXliffs


if __name__ == "__main__":
    argCount = len(sys.argv)
    if argCount >= 4:
        if "-g" == sys.argv[1]:
            generateExcel(sys.argv[2], sys.argv[3])
        elif "-r" == sys.argv[1]:
            mergeExcelToXliffs(sys.argv[2], sys.argv[3])
        else:
            print("请输入 -g 来生成或 -r来读取数据")
    else:
        print("缺少参数, eg: -g [xliffPath] [xlsxPath] or -r [xlsxPath] [xliffPath]")
    