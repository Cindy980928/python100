from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("logs")
'''
先介绍两个函数add_image和add_scalar的参数
add_image(self, tag, img_tensor, global_step=None, walltime=None, dataformats='CHW'):
    Add image data to summary.

    Args:
        tag (string): Data identifier
        img_tensor (torch.Tensor, numpy.array, or string/blobname): Image data  这里可以看到图片类型要求torch.Tensor或者numpy型
        global_step (int): Global step value to record
        walltime (float): Optional override default walltime (time.time())
          seconds after epoch of event

add_scalar(self, tag, scalar_value, global_step=None, walltime=None):
tag ： 图标的标题
scalar_value : x轴
global_step : y轴
'''

image_path = "../dataset/train/ants_image/0013035.jpg"
img_PIL = Image.open(image_path)  # 通过PIL获取的图像类型，type(img)输出<class 'PIL.JpegImagePlugin.JpegImageFile'>
img_array = np.array(img_PIL)  # 按照add_image对于图片类型的要求 转换为numpy类型

writer.add_image("test", img_array, 1, dataformats='HWC')  # 运行 在网页的Images选项下就能看到图片了

for i in range(100):
    writer.add_scalar("y=x", i, i)

writer.close()

'''
tensorboard端口查看 tensorboard --logdir=logs
注意：这里的logs是运行该文件后生成的logs文件夹，是相对于该py文件的路径，路径不对将会报错：No dashboards are active for the current data set.
此处应该为tensorboard --logdir=day16-20/logs
端口修改,避免和别人的端口冲突 tensorboard --logdir=day16-20/logs --port=6007


注意：
当修改writer.add_scalar("y=x", 2*i, i)
这里的tag"y=x"不改变时，会在同一个图表上绘制，并且图像会发生过拟合
'''
