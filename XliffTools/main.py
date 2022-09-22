# 当我们拿到一个项目时，首先要在项目运行环境安装 requirement.txt 所包含的依赖：
# pip install -r requirement.txt
# 当我们要把环境中的依赖写入 requirement.txt 中时，可以借助 freeze 命令：
# pip freeze >requirements.txt

import sys
from generate import generateExcel

if __name__ == "__main__":
    argCount = len(sys.argv)
    if argCount >= 2:
        generateExcel(sys.argv[1], None)
    if argCount >= 3:
        generateExcel(sys.argv[1], sys.argv[2])
    