Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@samanthalrobbins 
 The password you provided is weak and can be easily guessed. To increase your security, you must update your password. After April 23, 2020 we will automatically reset your password. Change your password on the settings page.

Read our documentation on safer password practices.

Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


evenegas3
/
StateFarmProject
Private
1
11
 Code Issues 0 Pull requests 1 Actions Projects 0 Security Insights
StateFarmProject/Code/sentiment.py /
@KyStro KyStro sentiment with TB and NLTK
c72e3ba 4 days ago
127 lines (98 sloc)  3.2 KB
  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:52:24 2020
@author: Kyle
"""

import pandas as pd
from textblob import TextBlob
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

'''
This module provides sentiment using 
TESTNAME: Name of cleaned csv file
SHOW_ALL: If True, shows all tweets, regardless of sentiment
NEUTRAL: Range to categorize tweet as negative (below first bound),
    neutral (equal to or above first bound but equal or lower than second bound),
    or positive (above second bound). Polarity scores are [-1,1].
SHOW_POSITIVE: If True, shows all positive sentiment tweets
SHOW_NEGATIVE: If True, shows all negative sentiment tweets
SUBJECTIVITY: Value set to determine how much emotion is in a tweet. [0,1]
SHOW_ABOVE_SUB: If True, only shows tweets with SUBJECTIVITY over above value.
'''
TESTNAME = 'clean_base.csv'
SHOW_ALL = True
NEUTRAL = (-0.5, 0.5)
SHOW_POSITIVE = True
SHOW_NEGATIVE = True
SUBJECTIVITY = 0.5
SHOW_ABOVE_SUB = True

def get_df(file):
    df = pd.read_csv(file, encoding='utf-8-sig')
    return df


def get_sentiment(tweet):
    pol = TextBlob(tweet).sentiment.polarity
    return pol

def get_nltk(tweet):
    d = SentimentIntensityAnalyzer().polarity_scores(tweet)
    return d['compound']

def get_subjectivity(tweet):
    sub = TextBlob(tweet).sentiment.subjectivity
    return sub

def verdict(n):
    if n < NEUTRAL[0]:
        return 'negative'
    elif n > NEUTRAL[1]:
        return 'positive'
    else:
        return 'neutral'

def add_senti_cols(df):
    df.drop(df[df['text'].isna()].index, inplace=True)
    data = [get_sentiment(t) for t in df['text']]
    df['polarity'] = data
    subs = [get_subjectivity(t) for t in df['text']]
    df['subjectivity'] = subs
    df['+/-'] = [verdict(n) for n in data]
    
    
    data2 = [get_nltk(t) for t in df['text']]
    df['nltk_polarity'] = data2
    df['nltk_verdict'] = [verdict(n) for n in data2]

    

def conditions(df):
    if SHOW_ALL:
        return
    
    if SHOW_POSITIVE and SHOW_NEGATIVE:
        drop_neutral(df)
        
    elif SHOW_POSITIVE:
        drop_neutral(df)
        drop_negative(df)
        
    elif SHOW_NEGATIVE:
        drop_neutral(df)
        drop_positive(df)
    else:
        drop_negative(df)
        drop_positive(df)
        
    if SHOW_ABOVE_SUB:
        drop_subjectivity(df)
    else:
        drop_subjectivity(df, up=False)
    

def drop_na(df):
    df.drop(df[df['polarity'].isna()].index, inplace=True)

def drop_neutral(df):
    df.drop(df[(df['polarity']>=NEUTRAL[0]) & (df['polarity']<=NEUTRAL[1])].index, inplace=True)

def drop_positive(df):
    df.drop(df[df['polarity']>NEUTRAL[1]].index, inplace=True)

def drop_negative(df):
    df.drop(df[df['polarity']<NEUTRAL[0]].index, inplace=True)
    
def drop_subjectivity(df, up=True):
    if up:
        df.drop(df[df['subjectivity']<=SUBJECTIVITY].index, inplace=True)
    else:
        df.drop(df[df['subjectivity']>SUBJECTIVITY].index, inplace=True)
    
def main():
    df = get_df(TESTNAME)
    add_senti_cols(df)
    drop_na(df)
    conditions(df)
    df.sort_values(['polarity'], inplace=True)
    df.to_csv('sentiment_'+TESTNAME[6:], index = False, encoding='utf-8-sig')

main()
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
