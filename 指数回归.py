# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/8 11:44
# @Function:指数回归
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义指数回归函数模型
def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

# 准备数据
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1, 3, 8, 20, 48, 115])

# 拟合指数回归模型
popt, pcov = curve_fit(exponential_func, x_data, y_data)

# 提取拟合参数
a = popt[0]
b = popt[1]
c = popt[2]

# 打印拟合参数
print("a =", a)
print("b =", b)
print("c =", c)

# 绘制原始数据和拟合曲线
x_range = np.linspace(0, 5, 100)
y_pred = exponential_func(x_range, a, b, c)

plt.scatter(x_data, y_data, label="Original Data")
plt.plot(x_range, y_pred, color='r', label="Exponential Regression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
'''
在上述代码中，我们首先定义了指数回归模型函数 exponential_func，其中 a、b 和 c 是指数回归的参数。
然后，我们准备了自变量 x_data 和因变量 y_data 的示例数据。
接下来，我们使用 curve_fit 函数进行拟合。该函数使用最小二乘法来拟合指定的函数模型到数据。它返回拟合参数 popt 和协方差矩阵 pcov。
在代码的最后部分，我们提取了拟合的参数，并使用这些参数生成拟合曲线。然后，我们使用 matplotlib 库绘制原始数据和拟合曲线的散点图。
运行以上代码将得到指数回归的拟合参数和绘制的拟合曲线图。请注意，这只是一个简单的示例，你可以根据实际问题和数据进行相应的调整和扩展。
'''