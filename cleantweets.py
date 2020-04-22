#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:47:48 2020

@author: samantharobbins
"""
import pandas as pd
import csv
#import re

'''
Reads in a file
'''
def read_file(file):
    df = pd.read_csv(file, encoding='utf-8-sig')
    return df

'''
This function checks tweets for text slang
'''
def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        fileName = "slang.txt"
        
        with open(fileName, "r") as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            #_str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
            for row in dataFromFile:
                if _str.upper() == row[0]:
                    user_string[j] = row[1]
            #myCSVfile.close()
        j = j + 1
    return ' '.join(user_string)

'''
this function iterates through each text to change the slang
'''
def transcheck(df):
    ls = []
    for i in df["text"]:
        ls.append(translator(i).lower())
    df["text"] = ls
    return df
'''
Replaces occurences of 'amp' and '&amp' with the word 'and'. This is because
of a encoding problem which turns '&' to 'amp' and/or '&amp'.
'''
def amp(df):
    df['text'] = df['text'].str.replace('&amp','and ')
    df['text'] = df['text'].str.replace('amp','and ')
    return df

def main():
    df = read_file('mobile19.csv')
    df = amp(df)
    df = transcheck(df)
    
    df.to_csv("clean_mobile19.csv", index = False, encoding='utf-8-sig')
    
if __name__ == '__main__':
    main()
