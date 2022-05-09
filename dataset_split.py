# -*- coding: utf-8 -*-

import argparse
import os
import random
import shutil

IMG_PATH = './datasets/images/'
IMG_PATH_TEMPLATE = IMG_PATH + '%s'
IMG_TRAINING_PATH = './datasets/images_training/'
IMG_VAL_PATH = './datasets/images_val/'

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_val', type=int, default=72, help='Number of images in validation set')
    args = parser.parse_args()
    
    file_list = os.listdir(IMG_PATH)
    training_set_list = file_list.copy()
    val_set_list = random.sample(file_list, args.num_val)
    for d in val_set_list:
        training_set_list.remove(d)
        d_path = IMG_PATH_TEMPLATE % d
        shutil.copy(d_path, IMG_VAL_PATH)
    for d in training_set_list:
        d_path = IMG_PATH_TEMPLATE % d
        shutil.copy(d_path, IMG_TRAINING_PATH)