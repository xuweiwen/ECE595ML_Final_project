# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def result_visualization(df):
    plt.rcParams["figure.figsize"] = (6,3)
    sns.lineplot(data=df, x='Epochs', y='PSNR', hue='Config')
    cf = plt.gcf()
    cf.savefig('psnr.pdf', bbox_inches='tight', format='pdf', dpi=1000)

p_n2n_psnr = []
p_n2c_psnr = []
g_n2n_psnr = []
g_n2c_psnr = []
with open('./results/p_n2n_log.txt','r') as raw:
    for line in raw:
        if len(line) < 30:
            p_n2n_psnr.append(float(line.split(': ')[1]))
    raw.close()
with open('./results/p_n2c_log.txt','r') as raw:
    for line in raw:
        if len(line) < 30:
            p_n2c_psnr.append(float(line.split(': ')[1]))
    raw.close()
with open('./results/g_n2n_log.txt','r') as raw:
    for line in raw:
        if len(line) < 30:
            g_n2n_psnr.append(float(line.split(': ')[1]))
    raw.close()
with open('./results/g_n2c_log.txt','r') as raw:
    for line in raw:
        if len(line) < 30:
            g_n2c_psnr.append(float(line.split(': ')[1]))
    raw.close()

#psnr = [p_n2n_psnr, p_n2c_psnr, g_n2n_psnr, g_n2c_psnr]
epoch = [i for i in range(100)]

structure = {'Config':[], 'Epochs':[], 'PSNR':[]}
df = pd.DataFrame(data=structure)

for i in range(100):
    #df.loc[len(df.index)] = ['Poisson, n2n', epoch[i], p_n2n_psnr[i]]
    #df.loc[len(df.index)] = ['Poisson, n2c', epoch[i], p_n2c_psnr[i]]
    df.loc[len(df.index)] = ['Gaussian, n2n', epoch[i], g_n2n_psnr[i]]
    df.loc[len(df.index)] = ['Gaussian, n2c', epoch[i], g_n2c_psnr[i]]

result_visualization(df)