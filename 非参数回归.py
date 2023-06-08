# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/8 11:53
# @Function:非参数回归
import numpy as np
import matplotlib.pyplot as plt

# 生成示例数据
np.random.seed(0)
X = np.linspace(-5, 5, 100)
Y = np.sin(X) + np.random.normal(0, 0.2, size=len(X))

# 定义局部加权回归函数
def locally_weighted_regression(x, X, Y, tau):
    m = len(X)
    W = np.exp(-(x - X)**2 / (2 * tau**2))
    W = np.diag(W)
    X_extended = np.column_stack((X, np.ones(m)))
    theta = np.linalg.inv(X_extended.T @ W @ X_extended) @ (X_extended.T @ W @ Y)
    return theta[0] * x + theta[1]

# 设定参数
tau = 0.5  # 高斯核带宽

# 对每个数据点进行局部加权回归
Y_pred = [locally_weighted_regression(x, X, Y, tau) for x in X]

# 绘制原始数据和回归曲线
plt.scatter(X, Y, label='Original Data')
plt.plot(X, Y_pred, color='r', label='Locally Weighted Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
'''
在上述代码中，我们首先生成了示例数据，其中 X 是自变量，Y 是因变量。
然后，我们定义了局部加权回归函数 locally_weighted_regression。
该函数使用高斯核来计算每个数据点的权重，并利用最小二乘法计算局部加权回归的参数。
接下来，我们设定了参数 tau，该参数控制了高斯核的带宽。
然后，我们对每个数据点 X 进行局部加权回归预测，得到回归预测值 Y_pred。
最后，我们使用 matplotlib 库绘制原始数据和回归曲线的散点图。
运行以上代码将得到非参数回归的拟合曲线图。请注意，非参数回归方法的优点是不对回归函
数形式做出假设，能够更灵活地适应数据分布，但计算复杂度较高。
你可以根据实际问题和数据调整参数 tau 来获得更好的拟合效果。
'''