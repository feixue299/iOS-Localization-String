# 导入pandas模块
import pandas as pd

from common import findXliff, mergeTransDataToXliff

# 第一个参数为Excel的路径
# 第二个参数为需要写入的xliff文件路径

def mergeExcelToXliffs(inputPath, outputPath):
    if inputPath == None or outputPath == None:
        print("缺少输入或输出路径")
        return
    # 把Excel文件中的数据读入pandas
    df = pd.read_excel(inputPath)
    langData = list(df.columns.array)
    langData.pop(0)
    print(f"langData:{langData}")
    transData = {}
    for indexs in df.index:
        rowData = df.loc[indexs]
        unit_id = rowData.values[0]
        lang_row = rowData.values[1:-1]
        trans_dic = {}
        for i in range(len(lang_row)):
            trans_dic[langData[i]] = lang_row[i]
        transData[unit_id] = trans_dic

    xliffs = findXliff(outputPath)

    for path in xliffs:
        mergeTransDataToXliff(langData, transData, path)
    
        
