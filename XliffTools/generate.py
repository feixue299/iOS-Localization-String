import pandas as pd
from openpyxl import Workbook
from common import findXliff, parseXliffPath

# 第一个参数为xliff的输入路径，如果路径为文件夹则查询该目录底下的所有xliff
# 第二个参数为输出的路径，路径存在则为尝试匹配原文件中字段，路径不存在则新建Excel
def generateExcel(inputPath, outputPath):
    if inputPath == None or outputPath == None:
        print("缺少输入或输出路径")
        return

    # key: 每个翻译条目, value: 各个语言的翻译
    transData = {}
    langData = []
    xliffs = findXliff(inputPath)
    
    for path in xliffs:
        parseXliffPath(path, langData, transData)

    openpyxlParse(outputPath, langData, transData)
    

# 使用openpyxl解析
def openpyxlParse(outputPath, langData, transData):
    excel_path = outputPath + "/ios.xlsx"
    workbook = Workbook()

    # 默认sheet
    sheet = workbook.active
    sheet.title = "默认sheet"
    sortLang(langData)
    

    sheet.append(["unit-id"] + langData)
    
    for key in transData:
        row_data = []
        row_data.append(key)
        for lang in langData:
            text = transData[key][lang]
            if text == None:
                text = ""
            text = text.strip('"')
            text = text.strip("'")
            row_data.append(text)
        sheet.append(row_data)
    
    workbook.save(excel_path)


# 排序语言
def sortLang(langData: list):
    advance("ru", langData)
    advance("pt-PT", langData)
    advance("pl", langData)
    advance("sv", langData)
    advance("nl", langData)
    advance("de", langData)
    advance("fr", langData)
    advance("it", langData)
    advance("es", langData)
    advance("zh-Hans", langData)
    advance("en", langData)


# 将lang提前
def advance(lang, langData):
    if lang in langData:
        langData.remove(lang)
        langData.insert(0, lang)


# 使用panda解析
def pandasParse(outputPath, langData, transData):
    csvpath = outputPath + "/ios.csv"
    csvfile = open(csvpath, "w")
    csvfile.write("unit-id\t")
    for lang in langData:
        csvfile.write(f"{lang}\t")
    csvfile.write("\n")

    for key in transData:
        csvfile.write(f"{key}\t")
        print(f"key:{key}")
        for lang in langData:
            text = transData[key][lang]
            if text == None:
                text = ""
            print(text)
            csvfile.write(f"{text}\t")
        csvfile.write("\n")
    csvfile.close()
    #该模块以弃用，建议使用openpyxl
    data = pd.read_csv(csvpath, sep="\t")
    excel_path = outputPath + "/ios.xls"
    data.to_excel(excel_path, index=False)
