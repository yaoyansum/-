# -*- coding: utf-8 -*-
# @Author  : yanyao
# @Time    : 2023/5/31 13:51
# @Function:
import os
from osgeo import ogr, gdal

# 输入矢量文件路径
vector_file = 'input.shp'

# 输出栅格图像路径
output_tiff = 'output.tif'

# 定义栅格化参数
pixel_size = 10  # 像元大小（单位：米）
output_width = 0  # 输出图像宽度（自动计算）
output_height = 0  # 输出图像高度（自动计算）

# 打开矢量文件
vector_ds = ogr.Open(vector_file)
layer = vector_ds.GetLayer()

# 获取矢量图层的范围
x_min, x_max, y_min, y_max = layer.GetExtent()

# 计算输出图像的宽度和高度
output_width = int((x_max - x_min) / pixel_size)
output_height = int((y_max - y_min) / pixel_size)

# 创建栅格图像
driver = gdal.GetDriverByName('GTiff')
output_ds = driver.Create(output_tiff, output_width, output_height, 1, gdal.GDT_Byte)

# 设置图像的地理转换参数和投影信息
output_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
output_ds.SetProjection(layer.GetSpatialRef().ExportToWkt())

# 使用栅格化算法将矢量数据栅格化到图像中
gdal.RasterizeLayer(output_ds, [1], layer, burn_values=[1])

# 释放资源
vector_ds = None
output_ds = None

print("转换完成！")
