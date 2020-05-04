import pandas as pd
import os, json, csv
from os import listdir
from os.path import isfile, join

collect = []

def rename_cols(state):
    """
    NOTE: DON'T CALL THIS


    Function is simply to rename columns to match a similar format from a previous tweetscraping library.
    Made so cleaning files don't need to be altered.
    """
    if ' ' in state:
        state = state.replace(' ', '')

    df = pd.read_csv('24km_{}.csv'.format(state), sep='\t')
    df = df.rename(columns={'username':'screen_name', 'to':'replay_to_users', 'date':'timestamp', 'id':'user_id', 'favorites':'likes', 'permalink':'tweet_url'})

    for row in df.loc[df.hashtags.isnull(), 'hashtags'].index:
        df.at[row, 'hashtags'] = []


    for i, row in df.iterrows():
        tags = row['hashtags']
        if tags != []:
            tags = tags.replace('#', '')
            df.loc[i, 'hashtags'] = tags

    df.to_csv('final_{}2019.csv'.format(state))


def delete_empty(state):
    """
    Function takes in a state name and checks directory for all city files for that state.
    If file is empty, then remove/delete it.

    This was created more as a sanity check, as sometimes a city file was created and it would be empty.
    Either because there is no avaliable data for that city, or a fetch limit was hit.
    """
    count = 0
    if ' ' in state:
        state = state.replace(' ', '')

    for file in os.listdir():
        if file.startswith(state) and file.endswith('.csv') and file != '{}.csv'.format(state):

            print(file)
            df = pd.read_csv(file)
            print(df)

            if len(df) < 1:
                count += 1
                os.remove(file)

    print(count)

def fetch_tweets(state, city, city_id, lat, lng):
    """
    Function checks to see whether a city file exists (ex: 'Michigan1840003938.csv').
    If it exists and isn't empty, append it to a list (collect), to later be concatenated by state.
    If it !exist, fetch twitter data.
    """
    if ' ' in state:
        state = state.replace(' ', '')

    if not '{}{}.csv'.format(state, city_id) in os.listdir():
        command = """GetOldTweets3 --querysearch "statefarm" --near "{}, {}" --within 24km --maxtweets 100000 --lang en \
                --since 2019-01-01 --until 2020-01-01 --output {}{}.csv""".format(str(lat), str(lng), state, city_id)
        os.system(command)

    if '{}{}.csv'.format(state, city_id) in os.listdir():
        df = pd.read_csv('{}{}.csv'.format(state, city_id))
        df['city_id'] = int(city_id)
        df['city'] = city
        df['lat'] = lat
        df['lng'] = lng
        df.to_csv('{}{}.csv'.format(state, city_id))

        if len(df) > 0:
            collect.append(df)


def real_main(state):
    world = pd.read_csv('worldcities.csv')
    us_df = world[world.country == 'United States']
    state_df = us_df[us_df.admin_name == state]

    for i, row in state_df.iterrows():
        city, city_id = row['city'], str(row['id'])
        lat, lng = str(row['lat']), str(row['lng'])
        # print(state, city, city_id, lat, lng)
        fetch_tweets(state, city, city_id, lat, lng)

    final_df = pd.concat(collect, axis=0, ignore_index=True)
    print(final_df)
    if ' ' in state:
        state = state.replace(' ', '')
    final_df.to_csv('24km_{}.csv'.format(state), sep='\t', encoding='utf-8')
    print('$$$$$')

s = 'Illinois'
delete_empty(s)
real_main(s)
