import pandas as pd

# 创建一个数据帧
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
        'Age': [25, 30, 35, 40],
        'Country': ['USA', 'Canada', 'UK', 'Japan']}
df = pd.DataFrame(data)

# 将数据写入Excel文件
df.to_excel('example.xlsx', index=False)