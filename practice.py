import os
import glob
import path
import cv2
import numpy as np
from collections import OrderedDict
import pickle

def main():
    train_path = "./mnist/train/"
    test_path = "./mnist/test/"

    train_paths = glob.glob(train_path + '/*/*')
    test_paths = glob.glob(test_path + '/*/*')

    train_dataset = read_image_and_label(train_paths)
    test_dataset = read_image_and_label(test_paths)

    save_npy(train_dataset, test_dataset)

    data_dict = read_npy()

    save_pickle(data_dict)

    image = data_dict['train_image'][0]

    data_augment(image)



def read_image_and_label(paths):
    # TODO: with image folders path, read images and make label with image paths)
    # DO NOT use dataset zoo from pytorch or tensorflow
    images = []
    labels = []
    for path in paths:
        label = path.split(os.path.sep)[1]
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        images.append(image)
        labels.append(label)
    return images, labels


def save_npy(train_dataset, test_dataset):
    train_images, train_labels = train_dataset
    test_images, test_labels = test_dataset

    np.save("./train_images.npy",train_images)
    np.save("./test_images.npy", test_images)
    np.save("./train_labels.npy", train_labels)
    np.save("./test_labels.npy", test_labels)

def read_npy():
    # TODO: read npy files and return dictionary
    train_images = np.load("./train_images.npy")
    train_labels = np.load("./train_labels.npy")
    test_images = np.load("./test_images.npy")
    test_labels = np.load("./test_labels.npy")
    """
     data = {'train image': [train_images],
             'train label': [train_labels],
             'test_image': [test_images],
             'test_label': [test_labels]
            }
    """
    data_dict = OrderedDict()
    data_dict['train_image'] = train_images
    data_dict['train_label'] = train_labels
    data_dict['test_image'] = test_images
    data_dict['test_label'] = test_labels
    return data_dict

def save_pickle(data_dict):
    # TODO: save data_dict as pickle (erase "return 0" when you finish write your code)
    with open('data.pickle', 'wb') as f:
        pickle.dump(data_dict, f)

def data_augment(image):
    # TODO: use cv2.flip, cv2.rotate, cv2.resize and save each augmented image
    cv2.imwrite("./original.jpg",image)
    image_1 = cv2.flip(image, 1)
    cv2.imwrite("./augmented_image_1.jpg",image_1)
    image_2 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("./augmented_image_2.jpg",image_2)
    image_3 = cv2.resize(image, (56, 56), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("./augmented_image_3.jpg",image_3)

if __name__ == "__main__":
    main()
