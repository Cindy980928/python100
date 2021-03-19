'''
用Pillow操作图像
文档：https://pillow-cn.readthedocs.io/zh_CN/latest/handbook/tutorial.html#
Pillow是由从著名的Python图像处理库PIL发展出来的一个分支
通过Pillow可以实现图像压缩和图像处理等各种操作。可以使用下面的命令来安装Pillow。

    pip install pillow

'''
from PIL import Image, ImageFilter

img = Image.open('img.jpg')
print(img.format, img.size, img.mode)
# img.show()

# 裁剪图像
rect = 80, 20, 210, 250
# img.crop(rect).show()

img.filter(ImageFilter.CONTOUR).show()

# 生成缩略图
size = 128, 128
img.thumbnail(size)
img.show()
