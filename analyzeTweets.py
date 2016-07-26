import json
import pandas as pd
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from collections import defaultdict
import SentimentClassifier

def getNeTree(tokenized_text):
	tagged_words = nltk.pos_tag(tokenized_text)
	neTree = nltk.ne_chunk(tagged_words, binary=False)
	return neTree

def getNeList(neTree):
	neList = []
	for subtree in neTree:
		if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
			ne_label = subtree.label()
			ne_string = " ".join([token for token, pos in subtree.leaves()])
			neList.append((ne_string, ne_label))
	return neList

def getNeDict(neList):
	neList_rev = [(b, a) for a, b in neList]
	neDict_temp = defaultdict(list)
	for k, v in neList_rev:
		neDict_temp[k].append(v)
	#neDict = dict((k, tuple(v)) for k, v in neDict_temp.iteritems())
	return neDict_temp

def nltkNer(tweet):
	text = tweet['text']
	tokenized_text = word_tokenize(text)
	neTree = getNeTree(tokenized_text)
	neList = getNeList(neTree)
	neDict = getNeDict(neList)
	#print(neDict['LOCATION'])
	tweet['PERSON'] = neDict['PERSON']
	tweet['ORGANIZATION'] = neDict['ORGANIZATION']
	tweet['LOCATION'] = neDict['LOCATION']
	#print neList

def classifyTweet(tweet, classifier):
	text = tweet['text']
	classification = classifier.classify(text)
	tweet['Sentiment'] = classification[0]


def processTweets(tweets_data_path):
	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	mySentimentClassifier = SentimentClassifier.VotedSentimentClassifier()
	for line in tweets_file:
		tweet = json.loads(line)

		# do ner on tweet
		nltkNer(tweet)

		# do sentiment analysis on tweet
		classifyTweet(tweet, mySentimentClassifier)

		tweets_data.append(tweet)

	tweets_file.close()
	return tweets_data


def pandizeTweets(tweets_data):

	tweets = pd.DataFrame()

	tweets['id'] = map(lambda tweet: tweet['id_str'], tweets_data)
	tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	tweets['PERSON'] = map(lambda tweet: tweet['PERSON'], tweets_data)
	tweets['ORGANIZATION'] = map(lambda tweet: tweet['ORGANIZATION'], tweets_data)
	tweets['LOCATION'] = map(lambda tweet: tweet['LOCATION'], tweets_data)
	tweets['Sentiment'] = map(lambda tweet: tweet['Sentiment'], tweets_data)
	print(tweets)
	return tweets

def writeTweetsToExcel(tweets):
	# Create a Pandas Excel writer using XlsxWriter as the engine.
	writer = pd.ExcelWriter('tweets.xlsx', engine='xlsxwriter')

	# Convert the dataframe to an XlsxWriter Excel object.
	tweets.to_excel(writer, sheet_name='Tweets')

	# Close the Pandas Excel writer and output the Excel file.
	writer.save()


if __name__ == '__main__':
	tweets_data_path = 'twitter_stream_1000tweets.txt'
	tweets_data = processTweets(tweets_data_path)
	tweets = pandizeTweets(tweets_data)
	writeTweetsToExcel(tweets)