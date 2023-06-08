# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/8 11:46
# @Function:对数回归
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 定义对数回归函数模型
def logistic_func(x, a, b):
    return 1 / (1 + np.exp(-(a * x + b)))

# 准备数据
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([0, 0, 1, 1, 1])

# 定义损失函数（负对数似然函数）
def loss_function(params):
    a = params[0]
    b = params[1]
    y_pred = logistic_func(x_data, a, b)
    loss = -np.mean(y_data * np.log(y_pred) + (1 - y_data) * np.log(1 - y_pred))
    return loss

# 随机初始化参数
initial_params = np.random.randn(2)

# 最小化损失函数
result = minimize(loss_function, initial_params, method='BFGS')
optimal_params = result.x

# 提取最优参数
a = optimal_params[0]
b = optimal_params[1]

# 打印最优参数
print("a =", a)
print("b =", b)

# 绘制原始数据和拟合曲线
x_range = np.linspace(0, 6, 100)
y_pred = logistic_func(x_range, a, b)

plt.scatter(x_data, y_data, label="Original Data")
plt.plot(x_range, y_pred, color='r', label="Logistic Regression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
'''
在上述代码中，我们首先定义了对数回归模型函数 logistic_func，其中 a 和 b 是对数回归的参数。
然后，我们准备了自变量 x_data 和因变量 y_data 的示例数据。
接下来，我们定义了损失函数，这里使用负对数似然函数作为损失函数。
然后，我们随机初始化参数，并使用 scipy.optimize.minimize 函数最小化损失函数。
该函数使用 BFGS（Broyden-Fletcher-Goldfarb-Shanno）算法进行优化，得到最优参数。
在代码的最后部分，我们提取了最优参数，并使用这些参数生成拟合曲线。然后，我们使用 matplotlib 库绘制原始数据和拟合曲线的散点图。
运行以上代码将得到对数回归的最优参数和绘制的拟合曲线图。请注意，这只是一个简单的示例，你可以根据实际问题和数据进行相应的调整和扩展。
'''

