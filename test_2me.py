# -*- coding: utf-8 -*-
# 在cmd中运行代码：python json2png.py <json文件夹>，单独运行这个文件会报错
import os
import subprocess
import glob
from osgeo import gdal
import shutil
import os
import cv2
import numpy as np
import os.path
# path = r'D:\pix4d\json'  # 这里是指.json文件所在文件夹的路径
# json_file = glob.glob(os.path.join(path, "*.json"))
#
# # 输入多行指令
# commands = [
#     "conda activate labelme"
# ]
# for path in json_file:
#     label="labelme_json_to_dataset "+path
#     commands.append(label)
#
# # 打开命令行会话
# command_session = subprocess.Popen("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#
# for command in commands:
#         command_session.stdin.write(command.encode())
#         command_session.stdin.write(b"\n")
#         command_session.stdin.flush()
#
# # 获取命令输出
# output = command_session.stdout.read()
# print(output.decode())
#
# # 关闭命令行会话
# command_session.stdin.close()
# command_session.wait()
# print("！！！！！！成功  json2png  ！！！！！！")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
path = r'D:\pix4d\json'
path2 =r'D:\pix4d\label_png'
# 获取文件夹下的所有文件名
files = os.listdir(path)
# 筛选出是文件夹的文件名
folder_names = [file for file in files if os.path.isdir(os.path.join(path, file))]
for dir_name in folder_names:
    source_file_path = os.path.join(path, dir_name)+'/label.png'
    destination_file_path = os.path.join(path2,dir_name)+'.png'
    shutil.copy2(source_file_path, destination_file_path)
# shutil.copy(path + eachfile + '/label.png', dirpath + eachfile.split('_')[0] + '.png')
# print(eachfile + ' successfully moved')
