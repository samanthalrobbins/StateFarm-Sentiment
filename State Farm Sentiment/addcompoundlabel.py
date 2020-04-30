#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:51:56 2020

@author: samantharobbins
"""

import pandas as pd
import ast
import numpy as np

def read_file(file):
    df = pd.read_csv(file)
    return df

def split(df):
    
    ls = []
    for i in df["score"]:
        res = ast.literal_eval(i) 
        ls.append(res)
        
    dfs = pd.DataFrame(ls)
    df["neg"] = dfs["neg"]
    df["neu"] = dfs["neu"]
    df["pos"] = dfs["pos"]
    df["compound"] = dfs["compound"]
    return df

def compdf(df):
    dfc = pd.DataFrame(df["compound"])
    return dfc

def label(df):
    df["label"] = df["compound"]
    
    mask = (df.label > 0.3)
    maskn = (df.label < -0.3)
    maskneu = (df.label > -0.3) & (df.label < 0.3)
    df['label'][mask] = "positive"
    df['label'][maskn] = "negative"
    df['label'][maskneu] = "neutral"
    #df.loc[(df.label > 0.3),'label']='positive' and df.loc[(df.label < -0.3),'label']='negative'
    return df
    
def combine(df, labeldf):
    df = df.drop(['compound'], axis = 1)
    final = pd.concat([df, labeldf], axis = 1)
    return final
    

def main():
    df = read_file("statefarm_sentiment.csv")
    split(df)
    cdf = compdf(df)
    #print(df)
    dfl = label(cdf)
    fdl=combine(df, dfl)
    fdl.to_csv(r'statefarm_compound.csv', index = False)

if __name__ == '__main__':
    main()
