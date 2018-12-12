import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing
import csv              # to perform operations on csv file
import nltk
# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

consumer_key = "2jKfIrZgM9kJz9F4XhilBXgi1"
consumer_secret = "nxtp2lKRJnX74Tq1Zh3Q24Ox0lh0B7XZGTd7tmQJDOjNR8uFIV"
access_token = "1017464608431341568-JkagP3u8mIqM95nGafFOeUZpXkVy3F"
access_secret = "k144fWX6blh4vcNRfhERXnhkvZcapgnojqg0PRJOIoOIx"

query='telangana elections'
count=2000
# We import our access keys:
#from credentials import *    # This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret) 

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# We create an extractor object:
extractor = twitter_setup()
searched_tweets = [status.full_text for status in tweepy.Cursor(extractor.search, q=query,lang='en',tweet_mode='extended').items(count)]

# split into words
from nltk.tokenize import word_tokenize
tokens = [word_tokenize(tweet) for tweet in searched_tweets]

# convert to lower case
tokens = [str(w).lower() for w in tokens]

# remove remaining tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])