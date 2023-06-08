# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/5/29 13:24
# @Function:气象数据NC文件监测
import netCDF4 as nc
import pandas as pd
import numpy as np

file = r'D:\oco2_LtCO2_181231_B11014Ar_221017173900s.SUB.nc4'
dataset =nc.Dataset(file)
all_vars=dataset.variables.keys()
print(all_vars)
###获取所有变量信息
all_vars_info = dataset.variables.items()
all_vars_info = list(all_vars_info)
print(all_vars_info)
###获取单独的一个变量的数据
# precipitationCal=dataset.variables['lat'][:]
# print(precipitationCal.shape)
# # 转换成数组
# var_data = np.array(precipitationCal)
# print(var_data)

