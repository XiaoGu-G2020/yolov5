import os
import shutil
import random
 
# 设置随机种子
random.seed(0)
 
 
def split_data(file_path,xml_path, new_file_path, train_rate, val_rate, test_rate):
    '''====1.将数据集打乱===='''
    each_class_image = []
    each_class_label = []
    for image in os.listdir(file_path):
        each_class_image.append(image)
    for label in os.listdir(xml_path):
        each_class_label.append(label)
     # 将两个文件通过zip（）函数绑定。
    data=list(zip(each_class_image,each_class_label))
    # 计算总长度
    total = len(each_class_image)
    # random.shuffle（）函数打乱顺序
    random.shuffle(data)
    # 再将两个列表解绑
    each_class_image,each_class_label=zip(*data)
 
    '''====2.分别获取train、val、test这三个文件夹对应的图片和标签===='''
    train_images = each_class_image[0:int(train_rate * total)]
    val_images = each_class_image[int(train_rate * total):int((train_rate + val_rate) * total)]
    test_images = each_class_image[int((train_rate + val_rate) * total):]
    train_labels = each_class_label[0:int(train_rate * total)]
    val_labels = each_class_label[int(train_rate * total):int((train_rate + val_rate) * total)]
    test_labels = each_class_label[int((train_rate + val_rate) * total):]
 
    '''====3.设置相应的路径保存格式，将图片和标签对应保存下来===='''
    # train
    for image in train_images:
        print(image)
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'train' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
 
    for label in train_labels:
        print(label)
        old_path = xml_path + '/' + label
        new_path1 = new_file_path + '/' + 'train' + '/' + 'labels'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + label
        shutil.copy(old_path, new_path)
    # val
    for image in val_images:
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'val' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
 
    for label in val_labels:
        old_path = xml_path + '/' + label
        new_path1 = new_file_path + '/' + 'val' + '/' + 'labels'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + label
        shutil.copy(old_path, new_path)
    # test
    for image in test_images:
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'test' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
 
    for label in test_labels:
        old_path = xml_path + '/' + label
        new_path1 = new_file_path + '/' + 'test' + '/' + 'labels'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + label
        shutil.copy(old_path, new_path)
 
 
if __name__ == '__main__':
    file_path = "E:\yolo_img\星天演武百晓生\images"
    xml_path = "E:\yolo_img\星天演武百晓生\labels"
    new_file_path = "E:\github_project\yolov5\datasets\mys"
    # 设置划分比例
    split_data(file_path,xml_path, new_file_path, train_rate=0.7, val_rate=0.1, test_rate=0.2)