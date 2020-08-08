from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from keras.datasets import mnist
from keras.utils import to_categorical
from keras import Sequential
from keras import backend as K
from readimg import get_data_labels
import numpy as np
import keras
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 设置全局变量
num_classes = 2  # 类别
batch_size = 128 # 批次大小
epochs = 12  # 训练多少次

# 设置图片维度
img_rows, img_cols = 125, 125  # 图片的大小


x_train, x_test, y_train, y_test = get_data_labels()

print(x_train.shape, x_test.shape)
input_shape = (125, 125, 1)


# 2. one-hot 编码
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# 构建卷积神经网络模型
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape)) # 32个过滤器，过滤器大小是3×3，32×26×26
model.add(MaxPooling2D(pool_size=(2, 2)))# 向下取样
model.add(Conv2D(64, (3, 3), activation='relu')) #64×24×24
model.add(MaxPooling2D(pool_size=(2, 2)))# 向下取样
model.add(Dropout(0.25))
model.add(Flatten()) #降维：将64×12×12降为1维（即把他们相乘起来）
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax')) #全连接2层
model.summary()

# 编译模型
model.compile(loss=keras.losses.binary_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])


# 神经网络
history = model.fit(x_train, y_train, batch_size=32, epochs=epochs, verbose=1, validation_data=(x_test, y_test))



