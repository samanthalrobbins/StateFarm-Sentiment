# StateFarm-Sentiment

In the Sentiment branch you will find three folders, one for each of the categories. 
They are oulined the same. 

The first file to run, is the sentiment.py. 
This file runs the (mobile, naturaldisasters, or statefarm).csv 

The imports necessary to run are as follows. 

import os
import re
import math
import string
import codecs
import json
from itertools import product
from inspect import getsourcefile
from io import open

This sentiment program is credited to:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

Installations to run the VADER SENTIMENT:
pip install vaderSentiment

or clone the repository from:
https://github.com/cjhutto/vaderSentiment

The files associated to run the sentiment.py are:
vader_lexicon.txt. -- the text file of lexicon punctuations of western style text inclusions such as :) is a smile face. It has known scoring of polarity and intensity. 

emoji_utf8_lexicon.txt -- the text file of emoji codes with scoring and insensity. 

This file returns a .csv file that adds the polarity scoring of the .csv that is hard coded in. 
So, (mobile, naturaldisaster, or statefarm)_sentiment.csv

The next file to run, is the addcompoundlabel.csv:
This file takes in the (mobile, naturaldisaster, or statefarm)_sentiment.csv
It reorganizes the score column to add individual scoring columns, pos, neg, neu, and compound score, as well as the compound label - positive, negative or neutral. 
It returns the (mobile, naturaldisaster, or statefarm)_compound.csv

Each category folder will include a Visualizations folder. That holds the associated visualization plots. 


