import argparse
from parse_strings import parse_file

def compare(dict1, dict2):

    diffDic1 = []
    diffDic2 = []

    key_group1 = [list(d.keys())[0] for d in dict1]
    key_group2 = [list(d.keys())[0] for d in dict2]

    key_group1 = sorted(key_group1, key=lambda x: x.lower())
    key_group2 = sorted(key_group2, key=lambda x: x.lower())

    for i in range(len(dict1)):
        key = list(dict1[i].keys())[0]
        if key not in key_group2:
            diffDic1.append(key)
    
    for j in range(len(dict2)):
        key = list(dict2[j].keys())[0]
        if key not in key_group1:
            diffDic2.append(key)

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
    file1_data = parse_file(args.file1)
    file2_data = parse_file(args.file2)
    diffDic1, diffDic2 = compare(file1_data, file2_data)
    
    print("file1_data.count:", len(file1_data), diffDic1, ", count:", len(diffDic1))
    print("--------------------------")
    print("file2_data.count:", len(file2_data), diffDic2, ", count:", len(diffDic2))