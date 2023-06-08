# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/6/6 12:04
# @Function:边缘检测
# @envi    :lableme
'''
osgeo库安装（其中包括GDAL）
conda install
To install this package run one of the following:
conda install -c conda-forge gdal
conda install -c "conda-forge/label/TEST" gdal
conda install -c "conda-forge/label/broken" gdal
conda install -c "conda-forge/label/cf201901" gdal
conda install -c "conda-forge/label/cf202003" gdal
conda install -c "conda-forge/label/gcc7" gdal
网站：https://anaconda.org/conda-forge/gdal
'''
import cv2
from osgeo import gdal, ogr, osr

def extract_object_boundary(input_path, output_path):
    # 读取输入的.tif图片
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # 对图像进行边缘检测
    #高斯滤波、计算梯度、非极大值抑制和双阈值处理
    # Canny边缘检测通常能够产生清晰的边界，并具有抑制噪声的能力。
    edges = cv2.Canny(image, 100, 200)

    '''
    # 应用Laplacian算子
    Laplacian算子对噪声比较敏感，因此在进行边缘检测之前，考虑对图像进行预处理，高斯模糊来抑制噪声。
    调整Laplacian函数的参数，例如使用不同的卷积核大小或数据类型（如cv2.CV_64F），以适应不同的图像和边缘检测需求。
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    

    # 应用Sobel算子
    sobel算子是一种基于梯度的边缘检测方法。
    在进行边缘检测之前，需要对图像进行预处理应用高斯模糊来抑制噪声
    需要调整合并边缘图像时的权重比例
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    
    
     # 定义Roberts算子核
    roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    # 应用Roberts算子
    edges_x = cv2.filter2D(image, -1, roberts_x)
    edges_y = cv2.filter2D(image, -1, roberts_y)
    # 合并x和y方向的边缘图像
    edges = cv2.addWeighted(edges_x, 0.5, edges_y, 0.5, 0)
    '''


    # 寻找边缘并创建矢量图层
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建矢量图层和要素
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataset = driver.CreateDataSource(output_path)
    spatial_ref = osr.SpatialReference()
    spatial_ref.ImportFromEPSG(4326)  # 设置坐标系（这里使用WGS84经纬度坐标系）
    layer = dataset.CreateLayer('boundary', spatial_ref, ogr.wkbPolygon)
    feature_defn = layer.GetLayerDefn()

    # 将边界信息转换为矢量要素并写入图层
    for contour in contours:
        polygon = ogr.Geometry(ogr.wkbPolygon)
        ring = ogr.Geometry(ogr.wkbLinearRing)
        for point in contour.squeeze():
            ring.AddPoint(point[0], point[1])
        polygon.AddGeometry(ring)

        feature = ogr.Feature(feature_defn)
        feature.SetGeometry(polygon)
        layer.CreateFeature(feature)
        feature = None

    # 释放资源
    dataset = None

# 指定输入和输出路径
input_path = 'path/to/your/input.tif'
output_path = 'path/to/your/output.shp'

# 调用函数提取物体边界并生成矢量图层
extract_object_boundary(input_path, output_path)
