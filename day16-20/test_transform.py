# transforms该如何使用
# 为什么需要Tensor数据类型
from PIL import Image
from torchvision import transforms

img_path = "../dataset/train/ants_image/0013035.jpg"
img = Image.open(img_path)

t = transforms.ToTensor()
t_img = t(img)

print(t_img)