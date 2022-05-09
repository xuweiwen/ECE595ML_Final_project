# -*- coding: utf-8 -*-

import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def result_visualization(df, x):
    plt.rcParams["figure.figsize"] = (6,3)
    sns.histplot(data=df, x=x, bins=10)
    cf = plt.gcf()
    cf.savefig('%s.pdf'%x, bbox_inches='tight', format='pdf', dpi=1000)

def build_df(d):
    structure = {'event':[], 'Event number':[], 'Event flow duration (s)':[]}
    df = pd.DataFrame(data=structure)
    for event in d.keys():
        if event != 'urban':
            df.loc[len(df.index)] = [event, d[event][0], d[event][1]]
    return df

if __name__=='__main__':
    
    with open('./datasets/event_stat', 'rb') as f:
        event_stat = pickle.load(f)
        f.close()
    event_stat_df = build_df(event_stat)
    result_visualization(event_stat_df, 'Event flow duration (s)')