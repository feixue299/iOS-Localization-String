import argparse
from parse_strings import parse_file

def compare(dict1, dict2):

    diffDic1 = []
    diffDic2 = []

    for i in range(len(dict1)):
        if list(dict1[i].keys())[0] not in [list(d.keys())[0] for d in dict2]:
            diffDic1.append(list(dict1[i].keys())[0])
    
    for j in range(len(dict2)):
        if list(dict2[j].keys())[0] not in [list(d.keys())[0] for d in dict1]:
            diffDic2.append(list(dict2[j].keys())[0])

    return diffDic1, diffDic2

if __name__ == "__main__":
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='Process some files.')

    # 添加参数
    parser.add_argument('file1', help='file1')
    parser.add_argument('file2', help='file2')

    # 解析参数
    args = parser.parse_args()

    # 获取参数值
    file1 = args.file1
    file2 = args.file2
    diffDic1, diffDic2 = compare(parse_file(file1), parse_file(file2))
    print(diffDic1)
    print(diffDic2)