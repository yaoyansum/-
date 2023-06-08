# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/8 11:44
# @Function:多项式回归
#设置——工具——python science
import numpy as np
import matplotlib.pyplot as plt

# 生成带噪声的示例数据
np.random.seed(0)
x_data = np.linspace(-5, 5, 100)
y_data = 3 * np.power(x_data, 3) + 2 * x_data + 1 + np.random.normal(0, 5, size=len(x_data))

# 拟合多项式回归模型
degree = 3  # 多项式的次数
coefficients = np.polyfit(x_data, y_data, degree)
poly_func = np.poly1d(coefficients)#回归公式

# 打印多项式系数
print("多项式系数:", coefficients)
#生成系数顺序为：最高次、次高、再者......常数

# 绘制原始数据和拟合曲线
x_range = np.linspace(-5, 5, 100)
y_pred = poly_func(x_range)

plt.scatter(x_data, y_data, label="Original Data")
plt.plot(x_range, y_pred, color='r', label="Polynomial Regression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
'''
在上述代码中，我们首先生成了带有噪声的示例数据。这里使用一个二次多项式作为真实模型，并添加正态分布的噪声。
然后，我们使用 np.polyfit 函数进行多项式回归拟合。该函数接受自变量 x_data、因变量 y_data 和多项式的次数 degree，并返回拟合的多项式系数。
接下来，我们使用 np.poly1d 函数创建一个多项式函数对象，以便可以通过该函数对象计算预测值。
在代码的最后部分，我们绘制了原始数据和拟合曲线的散点图。拟合曲线通过调用多项式函数对象来计算预测值。
运行以上代码将得到多项式回归的拟合系数和绘制的拟合曲线图。
请注意，这只是一个简单的示例，你可以根据实际问题和数据进行相应的调整和扩展，例如尝试不同的多项式次数或添加更多的特征变量。
'''
