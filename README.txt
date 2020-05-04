Details:
With Twitter's Official Search API you can only sent 180 Requests every 15 minutes. With a maximum number of 100 tweets per Request this means you 
can mine for 4 x 180 x 100 = 72.000 tweets per hour. Nor can you fetch tweets than a week. This python library 

Installation:
Use pip install GetOldTweets3
or pip install -e git+https://github.com/Mottl/GetOldTweets3#egg=GetOldTweets3

Python classes
Tweet: Model class that describes a specific tweet.

id (str)
permalink (str)
username (str)
to (str)
text (str)
date (datetime) in UTC
retweets (int)
favorites (int)
mentions (str)
hashtags (str)
geo (str)
TweetManager: A manager class to help getting tweets in Tweet's model.

getTweets (TwitterCriteria): Return the list of tweets retrieved by using an instance of TwitterCriteria.
TwitterCriteria: A collection of search parameters to be used together with TweetManager.

setUsername (str or iterable): An optional specific username(s) from a twitter account (with or without "@").
setSince (str. "yyyy-mm-dd"): A lower bound date (UTC) to restrict search.
setUntil (str. "yyyy-mm-dd"): An upper bound date (not included) to restrict search.
setQuerySearch (str): A query text to be matched.
setTopTweets (bool): If True only the Top Tweets will be retrieved.
setNear(str): A reference location area from where tweets were generated.
setWithin (str): A distance radius from "near" location (e.g. 15mi).
setMaxTweets (int): The maximum number of tweets to be retrieved. If this number is unsetted or lower than 1 all possible tweets will be retrieved.

Python Examples:
import GetOldTweets as got
tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama whitehouse")\
                                           .setMaxTweets(2)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)

CLI Examples:
$ GetOldTweets3 --querysearch "bitcoin" --near "Berlin, Germany" --within 25km --maxtweets 10 --output <file.csv>
$ GetOldTweets3 --username "barackobama" --since 2015-09-10 --until 2015-09-12 --maxtweets 10 --emoji unicode

