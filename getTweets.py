# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3300772537-UwfYYD7VWnW4O1KxKRgfjjhd6bTBSECgN8N95KP'
ACCESS_SECRET = 'D62GjVqvpsHPrFvL1qztCRYnrnqJsj9JRDJgdSmz4SKUi'
CONSUMER_KEY = 'iusl4lLcAfnidQ1RmYO3dD5NP'
CONSUMER_SECRET = 'HNQ3uTsUO1bv27CXzK4tuvIr9LLhPh2W9ovBFrWHYsPhYgEHFr'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample(language="en")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 10000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 