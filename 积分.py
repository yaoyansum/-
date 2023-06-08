# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/5/31 21:37
# @Function:积分
import numpy as np
from scipy.interpolate import griddata


# 读取二进制文件

file_path = r'D:\pix4d\Spectral_Response.csv'
data = np.genfromtxt(file_path, delimiter=',', encoding='utf-8')
# 根据第一维排序
sorted_data = data[data[:, 0].argsort()]

print(sorted_data)
zi=0
mu=0
for i in range(len(data[:,0])):
    zi+=data[i,0]*data[i,1]
    mu+=data[i,1]
lamt=zi/mu
print(zi,mu)
print(lamt)
# 定义插值点的网格
# xi = np.linspace(1, 5, 10)  # 插值点的x坐标范围
# #10为个数{1：5}
# yi = np.linspace(1, 5, 10)  # 插值点的y坐标范围
# xi, yi = np.meshgrid(xi, yi)  # 创建二维网格
#
# # 进行散点积分
# zi=
#
# # 打印结果
# print(zi)
