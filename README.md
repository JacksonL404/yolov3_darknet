# Yolov3适应darknet模型框架的pytorch版本

其中修改了原yolov3 v7.0版本的数据增强阈值 可以对小目标进行数据增强

发现了原yolov3的bug 单类别训练集conf很低

解决方法：创建一个dummyclass 将单类别变成两个类别进行训练
