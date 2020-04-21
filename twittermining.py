


import tweepy, json, csv, re
import GetOldTweets3 as got

CONSUMER_KEY = "XzeBZ4nozbWsmWIfF1uuYZse3"
CONSUMER_SECRET = "JwosRYgKCEA4lMAaGEqOSWqlgCmAcM7DiOKmf7EkM7R8p0PTNb"
ACCESS_KEY = "1224548885600669698-6cA8bAWg5bf1pTqdb0O3GQvUrHkyis"
ACCESS_SECRET = "Bq3mlHxxlzMNJDoHt7ry1Wg3kwDi5YQD1gwjaIIWIdx8Q"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search, wait_on_rate_limit=True, q='statefarm').items(10):
#     fields = tweet.__dict__.keys()
# for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(100):


def search_for_hashtags(hashtag_phrase):
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    #initialize Tweepy API
    api = tweepy.API(auth)
    
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % ("b"), 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])


#TODO: Implement a way to fetch older tweets between 2009-2019 without daily limit
def get_older_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('statefarm').setSince("2019-01-01").setUntil("2019-01-30").setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    # print(tweet)
    print(tweet.text)
    # print(tweetCriteria.)
    # tweetCrit = got.manager.TweetCriteria().

def test_for_geo():
    pass

def main():
    hashtag_phrase='statefarm'
    # search_for_hashtags(hashtag_phrase)
    #get_older_tweets()
    test_for_geo()

main()
