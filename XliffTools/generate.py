import string
from common import findXliff, parseXliffPath

# 第一个参数为xliff的输入路径，如果路径为文件夹则查询该目录底下的所有xliff
# 第二个参数为输出的路径，路径存在则为尝试匹配原文件中字段，路径不存在则新建Excel
def generateExcel(inputPath, outputPath):
    # key: 每个翻译条目, value: 各个语言的翻译
    transData = {}
    if inputPath == None:
        return
    xliffs = findXliff(inputPath)
    for path in xliffs:
        parseXliffPath(path, transData)
    print(f"transData:{transData}")