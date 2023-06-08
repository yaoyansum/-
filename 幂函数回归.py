# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/8 11:51
# @Function:
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义幂函数回归模型
def power_func(x, a, b):
    return a * np.power(x, b)

# 准备数据
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1, 4, 9, 16, 25])

# 拟合幂函数回归模型
popt, pcov = curve_fit(power_func, x_data, y_data)

# 提取拟合参数
a = popt[0]
b = popt[1]

# 打印拟合参数
print("a =", a)
print("b =", b)

# 绘制原始数据和拟合曲线
x_range = np.linspace(0, 6, 100)
y_pred = power_func(x_range, a, b)

plt.scatter(x_data, y_data, label="Original Data")
plt.plot(x_range, y_pred, color='r', label="Power Regression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
