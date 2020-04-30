#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:47:05 2020

@author: samantharobbins
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import csv
from matplotlib.pyplot import figure

def read_file(file):
    df = pd.read_csv(file, encoding='utf-8-sig')
    return df

def pie_count(df):
    labels = df["label"]
    pos = []
    neg = []
    neu = []
    for i in labels:
        if i == "positive":
            pos.append(i)
        if i == "negative":
            neg.append(i)
        if i == "neutral":
            neu.append(i)
            
    posc = len(pos)
    negc = len(neg)
    neuc = len(neu)
    #count = len(labels)
    
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [posc, negc, neuc]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, colors = ["mistyrose", "red", "lightslategrey"])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Natural Disaster Sentiment Breakdown", fontname = "Arial", fontsize = 15)
    plt.savefig('ndbreak.png', transparent=True, dpi = 100)
    plt.show()

def over_time(df):
    labels = df[["date","label"]]
    
    pos = ["negative", "neutral"]
    neg = ["positive", "neutral"]
    neu = ["positive", "negative"]
    
    posdf = labels[~labels["label"].str.contains("|".join(pos))]
    negdf = labels[~labels["label"].str.contains("|".join(neg))]
    neudf = labels[~labels["label"].str.contains("|".join(neu))]
    
    posdf["count"] = 1
    posdf["date"] =  pd.to_datetime(posdf["date"].values, format='%Y-%m-%d %H:%M:%S')
    posdf.set_index("date", inplace = True)
    posdf = posdf.groupby(posdf.index.month)['count'].sum()
    
    negdf["count"] = 1
    negdf["date"] =  pd.to_datetime(negdf["date"].values, format='%Y-%m-%d %H:%M:%S')
    negdf.set_index("date", inplace = True)
    negdf = negdf.groupby(negdf.index.month)['count'].sum()
    
    neudf["count"] = 1
    neudf["date"] =  pd.to_datetime(neudf["date"].values, format='%Y-%m-%d %H:%M:%S')
    neudf.set_index("date", inplace = True)
    neudf = neudf.groupby(neudf.index.month)['count'].sum()
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
    
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], labels = months, rotation = 45, fontname = "Arial")
   
    plt.plot(posdf, color = "mistyrose", linewidth = 4, label = "Positive")
    plt.plot(negdf, color = "red", linewidth = 4, label = "Negative")
    plt.plot(neudf, color = "lightslategrey", linewidth = 4 , label = "Neutral")
    plt.title("Natural Disaster Sentiment Over Time", fontname = "Arial", fontsize = 15 )
    plt.ylabel("Number of Tweets", fontsize = 10)
    plt.xlabel("Month", fontsize = 10)
    plt.legend()
    plt.tight_layout()
    plt.savefig('ndovertime.png', transparent=True, dpi = 100)
    plt.show()
    
def mean_compound(df):
    #df.index = pd.to_datetime(df.index,format='%m-%d')
    df = df.groupby(df.index.month)[ 'compound'].mean()
    df.index =  ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
    #df = df.set_index("month")
    return df
    
def mean_plot(df):
    
    comp = df[["date","label","compound"]]
    pos = ["negative", "neutral"]
    neg = ["positive", "neutral"]
    neu = ["positive", "negative"]
    
    posdf = comp[~comp["label"].str.contains("|".join(pos))]
    posdf["date"] =  pd.to_datetime(posdf["date"].values, format='%Y-%m-%d %H:%M:%S')
    posdf.set_index("date", inplace = True)
    posdf = mean_compound(posdf)
    
    negdf = comp[~comp["label"].str.contains("|".join(neg))]
    negdf["date"] =  pd.to_datetime(negdf["date"].values, format='%Y-%m-%d %H:%M:%S')
    negdf.set_index("date", inplace = True)
    negdf = mean_compound(negdf)
    
    neudf = comp[~comp["label"].str.contains("|".join(neu))]
    neudf["date"] =  pd.to_datetime(neudf["date"].values, format='%Y-%m-%d %H:%M:%S')
    neudf.set_index("date", inplace = True)
    neudf = mean_compound(neudf)
    
    
    
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    neg = negdf.clip(upper = 0)
    pos = posdf.clip(lower = 0)
    neu= neudf.clip(upper = 0.5, lower = -0.5)
    y1 = pos
    y2 = neg
    y3 = neu
    fig, ax = plt.subplots()
   
    plt.figure(figsize=(11,6), linewidth = 5)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], x ,rotation=45)
    y1.plot.area(color = "mistyrose",label = "Positive", linewidth=1)
    ax.set_prop_cycle(None)
    y2.rename(columns=lambda x: '_' + x).plot.area(label = "Negative", linewidth=1, color = "lightslategrey")
    ax.set_prop_cycle(None)
    y3.rename(columns=lambda x: '_' + x).plot.area(label = "Neutral", linewidth=1, stacked = False, color = "red")
    #ax.stackplot(x, y1, y2, y3)
    plt.ylim([-1.0, 1.0])
    plt.xticks(rotation=45)
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 1
    plt.title("Natural Disaster Sentiment Mean vs Month", fontname = "Arial", fontsize = 15)
    plt.xlabel('Month', fontsize = 10)
    plt.ylabel('Compound Sentiment Score / Mean', fontsize = 10)
    plt.legend()
    plt.tight_layout()
    plt.savefig("ndmean.png", transparent=True, dpi = 100)
    plt.show()
    

def main():
    df = read_file("naturaldisasters_compound.csv")
    #count = pie_count(df)
    #time = over_time(df)
    print(mean_plot(df))

if __name__ == '__main__':
    main()
