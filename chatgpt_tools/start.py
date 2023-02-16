import os
import sys

# 获取命令行输入的路径
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print("请提供需要遍历的文件夹路径")
    sys.exit()

# 创建一个字典，用于存储文件夹信息
folders_dict = {}

# 遍历文件夹
for root, dirs, files in os.walk(path):
    for dir_name in dirs:
        # 如果文件夹名以.lproj结尾
        if dir_name.endswith('.lproj'):
            # 获取文件夹名（去掉.lproj后缀）
            folder_name = dir_name[:-6]
            # 如果字典中不存在该文件夹名，则创建一个对应的key和value数组
            if folder_name not in folders_dict:
                folders_dict[folder_name] = []
            # 将该文件夹路径添加到对应的value数组中
            folders_dict[folder_name].append(os.path.join(root, dir_name))

# 打印字典
print(folders_dict)