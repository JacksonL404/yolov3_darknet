# 将yolov3-v6.0训练成的.pt文件，转换成为darknet框架下的.weights保存

from models import *
# 注意找到工程文件中有没有 models.py文件 例如下面Darknet save_weights函数都在models.py文件里定义好了  直接调用就好
# 注意：新建的pt2weights.py与models.py在同一目录下
model = Darknet("cfg/yolov3-2cls.cfg")  # 训练时候用的cfg 改成自己.cfg的地址
# load_darknet_weights(model,"weights/latest.pt")
# save_weights(model,path='weights/latest.weights',cutoff=-1)

checkpoint = torch.load("weights/flytest1080_0710/best.pt", map_location='cpu')  # 导入训练好的.pt文件 改成自己的.pt文件地址
model.load_state_dict(checkpoint['model'])
save_weights(model, path='weights/flytest1080_0710_best.weights', cutoff=-1)  # 生成.weights文件 改成自己的地址
