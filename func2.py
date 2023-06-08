# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/5/29 13:24
# @Function:气象数据NC文件监测
'''
netCDF4库安装
pip install netCDF4-1.6.3-cp310-cp310-win_amd64.whl
cp310表示python解译器版本
amd64表示计算机64位操作系统
'''
import netCDF4 as nc

# 打开NetCDF文件
filename = "your_file.nc"
data = nc.Dataset(filename)

# 输出文件信息
print("文件信息：")
print(data)

# 输出变量列表
print("\n变量列表：")
for var in data.variables:
    print(var)

# 读取和输出变量数据
print("\n变量数据：")
for var in data.variables:
    print(f"\n变量名：{var}")
    print(f"数据维度：{data.variables[var].dimensions}")
    print(f"数据值：\n{data.variables[var][:]}")

# 关闭文件
data.close()

