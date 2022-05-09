# -*- coding: utf-8 -*-

import argparse
import os
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
import pickle

EVENT_DATA_PATH = './datasets/events/'
EVENT_DATA_PATH_TEMPLATE = EVENT_DATA_PATH + '%s'
IMG_PATH_TEMPLATE = './datasets/images/%s_%d.jpg'

def extract_data(filename):
    infile = open(filename, 'r')
    timestamp = []
    x = []
    y = []
    pol = []
    num_event = 0
    for line in infile:
        num_event += 1
        words = line.split()
        timestamp.append(float(words[0]))
        #x.append(int(words[1]))
        #y.append(int(words[2]))
        #pol.append(int(words[3]))
    infile.close()
    return timestamp, x, y, pol, num_event

def save_image(args, data, imgpath):
    fig = plt.figure(frameon=False)
    fig.set_size_inches(args.img_size[1] / args.dpi, args.img_size[0] / args.dpi)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.axis('off')
    fig.add_axes(ax)
    maxabsval = np.amax(np.abs(data))
    ax.imshow(data, cmap='gray', clim=(-maxabsval,maxabsval))
    cf = plt.gcf()
    cf.savefig(imgpath, dpi=args.dpi)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_frame', type=int, default=30, help='Number of frames from one event flow')
    parser.add_argument('--num_frame_event', type=int, default=20000, help='Number of events used')
    parser.add_argument('--img_size', type=tuple, default=(180,240), help='Image size')
    parser.add_argument('--dpi', type=int, default=100, help='DPI')
    args = parser.parse_args()
    event_stat = {}
    file_list = os.listdir(EVENT_DATA_PATH)
    #file_list = ['urban.txt']###
    file_list_loop = tqdm(file_list)
    for file_name in file_list_loop:
        file_list_loop.set_description('Processing {}'.format(file_name))
        file_path = EVENT_DATA_PATH_TEMPLATE % file_name
        timestamp, x, y, pol, num_event = extract_data(file_path)

        event_name = os.path.splitext(file_name)[0]

        event_stat[event_name] = (num_event, timestamp[-1]-timestamp[0])
        '''
        event_interval = int(num_event / (args.num_frame+1))
        for i in range(args.num_frame):
            start_point = (i+1) * event_interval
            img = np.zeros(args.img_size, np.int64)
            for j in range(start_point, start_point + args.num_frame_event):
                img[y[j],x[j]] += (2*pol[j]-1)

            img_path = IMG_PATH_TEMPLATE % (event_name, i)
            save_image(args, img, img_path)
            '''
    with open('./datasets/event_stat', 'wb') as f:
        pickle.dump(event_stat, f)
        f.close()
    print(event_stat)