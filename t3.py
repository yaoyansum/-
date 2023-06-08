# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/2 18:50
# @Function:提取比辐射率，积分
import numpy as np
import os
import glob

def get_files_by_extension(folder_path, extension):
    # 使用glob模块获取文件夹下指定扩展名的文件路径列表
    file_pattern = os.path.join(folder_path, f"*.{extension}")
    files = glob.glob(file_pattern)

    # 返回文件路径列表
    return files

def read_txt_file(file_path):
    # 使用NumPy的loadtxt函数读取txt文件，并指定分隔符为逗号（或其他合适的分隔符）
    # data = np.loadtxt(file_path, dtype=np.float32,delimiter=',')
    data = np.loadtxt(file_path)
    # 返回读取的数据作为数组
    return data

if __name__ == '__main__':
    file_path = r'D:\pix4d\典型地物波普曲线\Spectral_Response.csv'
    data = np.genfromtxt(file_path, delimiter=',', encoding='utf-8')
    # 根据第一维排序
    sorted_data = data[data[:, 0].argsort()]
    ###############################################
    mu=0
    for i in range(len(data[:, 0])):
        mu += data[i, 1]

    ##########查找所有文件下txt文件#############################

    folder_path=r'D:\pix4d\典型地物波普曲线'
    out_txt=get_files_by_extension(folder_path,'txt')

    #####读取txt文件主程序################################
    for i in range(len(out_txt)):
        file_path=out_txt[i]
        data_array = read_txt_file(file_path)
        locals()[f'num_{i}']=[]
        if data_array[0,0]==7.0:
            zi=0
            for j in range(len(data_array[:,0])-1):
                yi = np.linspace(data_array[j,1],data_array[j+1,1]-0.1 , 10)  # 插值点的y坐标范围
                # 通过调用read_txt_file函数读取txt文件，并将返回的数组保存在变量中
                for k in range(10):
                    locals()[f'num_{i}'].append(yi[k])
            locals()[f'num_{i}'].append(data_array[len(data_array[:,0])-1,1])

            locals()[f'num_{i}']=np.array(locals()[f'num_{i}'])
            for m in range(len(sorted_data[:,1])):
                zi=locals()[f'num_{i}'][m]*sorted_data[:,1][m]
            # print(file_path,zi/mu)
            print("分子：{}#####分母：{}".format(zi,mu))
            print("####################################################")

