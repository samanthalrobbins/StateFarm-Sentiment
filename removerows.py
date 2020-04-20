#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program removes any unnecessary rows from an input csv file
of tweets. Examples of what are excluded:
    
    * Out of context reply tweets
    * Suspected State Farm accounts
    * Tweets that contain links
    * Duplicate tweets (all occurences)
    * Tweets relating to sports
    * Tweets that contain suspected spam or advertisement lingo
    * Tweets that are not in English
    
In addition to the above, tweets are also put into lowercase and
'@' characters are removed.
The program then makes a new .csv file of the rows that remain named:
    
    'removal-<TEST_NAME>.csv'
    
"""


import pandas as pd
from langdetect import detect, DetectorFactory, detect_langs

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Put .csv file here
TESTNAME = '05-2019.csv'

'''
This function takes in a csv file and converts it into a Pandas
dataframe. The 'permalink' column is dropped and the dataframe is
returned
'''
def read_file(file):
    df = pd.read_csv(file)
    df = pd.read_csv(file, encoding='utf-8-sig')
    df = df.drop("permalink",axis = 1)
    return df

'''
This function takes in a dataframe and drops all tweets that are replies
to another user. The 'to' column is then dropped all together. The dataframe
is returned.
'''
def remove_mentions(df):
    todf = df[~df['to'].isna()]
    df = pd.concat([df, todf]).drop_duplicates(keep=False)
    df =df.drop("to", axis = 1)
    return df

'''
Takes a dataframe and changes the tweet column to all lowercase.
The dataframe is returned.
'''
def make_lower(df):
    df["text"] = df["text"].str.lower()
    return df


'''
Takes a dataframe and drops tweets that are null and tweets from the
offical State Farm Twitter account. The dataframe is returned.
'''
def remove_sf_user(df):
    df.drop(df[df['username'] == 'StateFarm'].index, inplace=True)
    assert('StateFarm' not in df['username'])
    df.drop(df[pd.isna(df['text'])].index, inplace=True)
    return df


'''
Takes a dataframe and drops users that we suspected to be spam accounts
and would affect the sentiment as a whole. Returns the dataframe.
'''
def remove_sf_agents(df):
    employees = ["StateFarm", "SFAgent", "SF", "StFarm", "State_Farm", "statefarm", "MsCeeJay", "Agent", "agent", "PeaceMakerMN", "StLife_Ministry", "joshua042042", "dew_hayes", "SteveKreis23", "AWLwarsaw", "TeamBoychuck", "NormanSThomas", "SupHero2KidsOH", "mattdoughertysf", "InsWithDane", "sf", "insuredwithsam", "scrowl72", "SteveLittleInc", "KMADDIE72", "ThePridePages", "GumptownM", "chamber", "Chamber", "Josh_Hemphill_", "stfarm", "TylerPeschong", "acalvio", "ryguy_73", "TheBlock__", "BCIdentity", "WSNCT", "ANTDOGG422", "CHACHA555", "BurtchWorks", "BeefnSushi", "AmberInsuresMe", "SoldbySarahKemp", "EasternCareer", "PKWEnterprises", "FollowT34731484", "NHCOhelps", "newroads20", "BrandonHuffman9", "Phil_Mormann", "OntraMarketing", "LoveAlexissss_", "TurningPointDV", "GeorgeMentz", "cealiv", "Insurance", "insurance", "INC", "Inc", "NLWaugh83", "lesliecarrillo_", "TannerCobun", "mowsummerville1", "YO_Ant2", "joshkerr12", "idance2slick", "LISCChicago", "sono23", "SliceoftheHill", "andrea_keyo", "UConnHuskyGames", "nahokuahlo", "PGAGolfChat", "WorldLongDrive", "clearsurance", "koforadio", "emm4white", "SPARC_Hope", "HabitotMuseum", "MoringChris", "LISCChicago", "TheBurnRadio", "B103_FM", "DJKingBori", "ItsSev_", "zoglassie", " lgoldrick25", "eggosupplies", "Kassie_121", "SweetwaterTXedc", "TiffinUCareer", "BradleyBeckAgcy", "hardincountylib", "HogbackBbqPit", "essencefest", "rnb_001", "wecovernc", "ssgyeet", "BayState_Flower", "montinix3", "zacjonesstatef1", "WaterforLife68", "InsuringBuffalo", "MATTER_ngo", "standpointmn", "AppalCART", "WelcomeBasket", "billyhon_", "HCCapopka" ,"SMToddLedet", "K96Radio", "sjkids1849", "cktstour", "ksuengaged", "PinnacleMtnView", "HIPHOPSISTERS"]
    df = df[~df['username'].str.contains("|".join(employees))]
    return df

'''
Takes a dataframe and drops all tweets that contain a link.
A link is defined as containing 'http' in the tweet. The dataframe
is returned.
'''
def remove_links(df):
    df = df[~df['text'].str.contains("http")]
    return df

'''
Makes a new column that holds the original tweet - used later for the sentiment
'''
def copy(df):
    df["original"] = df["text"]
    return df


'''
Takes a dataframe and drops all tweets that are duplicate entries.
This is to reduce spam and advertisement in the sentiment. The dataframe
is returned.
'''
def remove_dup_spam(df):
    df = df.drop_duplicates(subset= ["text"], keep=False)
    return df

'''
Takes a dataframe and replaces all occurences of '@StateFarm' and
'@' with an empty stirng. The dataframe is returned.
'''

def remove_at(df):
    df['text'] = df['text'].str.replace('@StateFarm','')
    df['text'] = df['text'].str.replace('@','')
    return df
    
'''
Takes a dataframe and removes any tweet that mentions key 'sport words'. This is
due to State Farm's involvement with celebrities and sporting events. The dataframe
is returned.
'''
def remove_sport(df):
    sportwords = ["cp3","stephencurry30","state farm center","aaronrodgers12","march madness", "illini","halftime","half court","football","espn", "sugarbowl", "sugar bowl", "ogletree","qb","lakers" "basketball","sixers","knicks", "arena", "jimmy butler", "jb", "jimmy", "butler", "chris paul", "draft","atl", "atlanta", "nba", "stadium","sport","redskins","hawks", "seahawks", "lebron","harden","james harden","jharden13," ,"aaron rodgers", "patrick mahomes", "chris paul", "sugarbowl", "sugar bowl", "ogletree","qb","Lakers", "basketball","sixers","knicks", "arena", "jimmy butler", "jb", "jimmy", "butler", "chris paul", "draft","atl", "atlanta", "nba", "stadium","sport","redskins","hawks", "seahawks", 'celtics', 'nets', 'knicks', '76ers', 'raptors', 'warriors', 'clippers', 'lakers', 'suns', 'kings', 'bulls', 'cavaliers', 'pistons', 'pacers', 'bucks', 'mavericks', 'rockets', 'grizzlies', 'hornets', 'spurs', 'hawks', 'bobcats', 'heat', 'magic', 'wizards', 'nuggets', 'timberwolves', 'thunder', 'trail blazers', 'jazz', 'bills', 'dolphins', 'jets', 'patriots', 'bengals', 'browns', 'ravens', 'steelers', 'colts', 'jaguars', 'texans', 'titans', 'broncos', 'chargers', 'chiefs', 'raiders', 'eagles', 'giants', 'redskins', 'cowboys', 'bears', 'lions', 'packers', 'vikings', 'buccaneers', 'falcons', 'panthers', 'saints', '49ers', 'cardinals', 'rams', 'seahawks', 'braves', 'marlins', 'mets', 'phillies', 'nationals', 'cubs', 'reds', 'brewers', 'pirates', 'cardinals', 'diamondbacks', 'rockies', 'dodgers', 'padres', 'giants', 'orioles', 'white sox', 'yankees', 'rays', 'blue jays', 'red sox', 'indians', 'tigers', 'royals', 'twins', 'astros', 'angels', 'athletics', 'mariners', 'rangers']
    esport=["drlupo", "lupo", "dr lupo", "esports"]
    df = df[~df['text'].str.contains("|".join(sportwords))]
    df = df[~df['text'].str.contains("|".join(esport))]
    return df

'''
Takes a dataframe and drops all phrases that we considered to be linked with
spam or advertising. The dataframe is returned.
'''
def remove_random(df):
    jake = ["jake", "jakes"]
    terms = ["she shed", "five years in a row", "Five Years in a Row", "#1 in customer satisfaction", "reminder, if you", "watch the newest", "Happy New Year from", "congratulations to", "$10 donation", "donate $10", "blockchain", "cp3", "carrieunderwood"]
    df = df[~df['text'].str.contains("|".join(jake))]
    df = df[~df['text'].str.contains("|".join(terms))]
    return df

'''
Takes string 's' and returns 'True' if the tweet is in English; 'False' if
not.
'''
def is_english(s):
    try:
        return detect(s) == 'en'
    except:
        return False
    
    
'''
Takes a dataframe and drops all tweets that are not in English. The dataframe
is returned.
'''
def drop_non_en(df):
    
    for row in df.index:
        if not is_english(df.loc[row,'text']):
            df.drop(row, inplace=True)
    return df



def main():
    df = read_file(TESTNAME)
    df = remove_mentions(df)
    df = copy(df)
    df = make_lower(df)
    df = remove_sf_user(df)
    df = remove_sf_agents(df)
    df = remove_links(df)
    df = remove_dup_spam(df)
    df = remove_at(df)
    df = remove_sport(df)
    df = remove_random(df)
    df = drop_non_en(df)
    df.to_csv('removal'+TESTNAME, index = False, encoding='utf-8-sig')

if __name__ == '__main__':
    main()
