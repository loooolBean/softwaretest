'''
    Excel文件读写 ：
        1. 获取excel文件
        2. 获取sheet页
        3. 获取单元格内容
'''

import openpyxl

# 获取excel文件
excel = openpyxl.load_workbook('../data/Excel数据驱动.xlsx')

# sheet页的获取
sheet = excel['Sheet1']

# 获取指定单元格的内容
cell = sheet['A1'].value
print(cell)
