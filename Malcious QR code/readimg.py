from keras.preprocessing import image
from PIL import Image
from sklearn.model_selection import train_test_split
import os
import random
import numpy as np

data = []
labels = []

def readImg(path, name):
    img = Image.open(os.path.join(path, name))
    img = image.img_to_array(img)
    return img

def getImg(data, labels):
    for path in ["good", "bad"]:
        files = os.listdir(path)
        for file in files:
            data.append(readImg(path, file))
            if path == "good":
                labels.append(1)
            elif path == "bad":
                labels.append(0)
    
    # 打乱顺序
    c = list(zip(data, labels))
    random.shuffle(c)
    a, b = zip(*c)
    data, labels = list(a), list(b)

    return np.array(data), np.array(labels)


def get_data_labels():
    global data
    global labels
    data, labels = getImg(data, labels)

    X_train, X_test, y_train, y_test = train_test_split(data, labels, 
                                                       test_size=0.3, random_state=0, shuffle=True, 
                                                       stratify=labels)  
    
    return X_train, X_test, y_train, y_test
