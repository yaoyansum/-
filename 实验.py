# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/2 20:41
# @Function:
import numpy as np
arr=([1,2,3,4,5])
for j in range(len(arr)-1):
    xi = np.linspace(arr[j],arr[j+1]-0.1, 10)

    print(xi)