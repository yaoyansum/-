# @Author  : yanyao
# @Time    : 2023/5/30 11:08
# @Function:  json2png批处理
import os
import subprocess
import glob
import shutil
import os
import cv2
import numpy as np

def json2png():
    path = r'D:\pix4d\json'  # 这里是指.json文件所在文件夹的路径
    json_file = glob.glob(os.path.join(path, "*.json"))

    # 输入多行指令
    commands = [
        "conda activate labelme"
    ]
    for path in json_file:
        label = "labelme_json_to_dataset " + path
        commands.append(label)

    # 打开命令行会话
    command_session = subprocess.Popen("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    for command in commands:
        command_session.stdin.write(command.encode())
        command_session.stdin.write(b"\n")
        command_session.stdin.flush()

    # 获取命令输出
    output = command_session.stdout.read()
    print(output.decode())

    # 关闭命令行会话
    command_session.stdin.close()
    command_session.wait()
    print("！！！！！！成功  json2png  ！！！！！！")


####test.bat脚本发
#bat放在json文件夹里
# @echo off
# for %%i in (*.json)  do labelme_json_to_dataset %%i
# pause
#在指定环境中运行bat


# 将标签图从json文件中批量取出
def out_png():

    path = r'D:\pix4d\json'
    path2 = r'D:\pix4d\label_png'
    # 获取文件夹下的所有文件名
    files = os.listdir(path)
    # 筛选出是文件夹的文件名
    folder_names = [file for file in files if os.path.isdir(os.path.join(path, file))]
    for dir_name in folder_names:
        source_file_path = os.path.join(path, dir_name) + '/label.png'
        destination_file_path = os.path.join(path2, dir_name) + '.png'
        shutil.copy2(source_file_path, destination_file_path)
    print('！！！！！！！！！完成转移！！！！！！！！！')

##ground_truth转换为8位的单通道黑白图像
def ground_trut():
    bace_path = r"D:\pix4d\label_png"
    save_path = r'D:\pix4d\train'

    for im in os.listdir(bace_path):
        img = cv2.imread(os.path.join(bace_path, im))
        b, g, r = cv2.split(img)
        r[np.where(r != 0)] = 255
        cv2.imwrite(os.path.join(save_path, im), r)
    print("！！！！！！！！！!二值化！！！！！！！！")

if __name__ == '__main__':
    # json2png()
    # out_png()
    ground_trut()
    print("##############################################################")
