from torch.utils.data import Dataset
from PIL import Image
import os

'''
来自b站up主：我是土堆
b站视频：https://www.bilibili.com/video/BV1hE411t7RN?p=7

数据集：
链接：https://pan.baidu.com/s/1R5mBwBo-AGydrwZX0EDbCA 
提取码：tkrp

PyTorch是一个开源的Python机器学习库
'''


class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)  # 拼起来就是图片文件夹的路径
        self.image_path = os.listdir(self.path)  # 图片文件夹下所有图片路径的列表

    def __getitem__(self, index):
        image_name = self.image_path[index]
        image_item_path = os.path.join(self.root_dir, self.label_dir, image_name)
        img = Image.open(image_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.image_path)


def main():
    root_dir = "E:\\code\\python_study\\dataset\\train"
    ants_label_dir = "ants_image"
    bees_label_dir = "bees_image"
    ants_dataset = MyData(root_dir, ants_label_dir)
    bees_dataset = MyData(root_dir, bees_label_dir)
    train_dataset = ants_dataset + bees_dataset
    print("蚂蚁数据集长度%d 蜜蜂数据集长度%d train_dataset长度%d" % (len(ants_dataset), len(bees_dataset),len(train_dataset)))
    img, label = train_dataset[124]  # 重写了__getitem__方法，通过[]取值时返回的是img,label
    img.show()


if __name__ == '__main__':
    main()
