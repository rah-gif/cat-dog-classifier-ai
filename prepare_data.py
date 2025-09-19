import os
import cv2
import numpy as np

def load_images(folder_path, label):
    data = []
    for img_file in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_file)
        try:
            img = cv2.imread(img_path)
            img = cv2.resize(img, (64, 64))
            data.append((img, label))
        except:
            pass
    return data

def prepare_dataset():
    train_data = []

    # Load cat and dog images
    train_data += load_images("data/train/cats", 0)  # 0 = cat
    train_data += load_images("data/train/dogs", 1)  # 1 = dog

    # Shuffle and split
    np.random.shuffle(train_data)
    X, y = [], []
    for features, label in train_data:
        X.append(features)
        y.append(label)

    X = np.array(X) / 255.0  # Normalize
    y = np.array(y)

    return X, y
