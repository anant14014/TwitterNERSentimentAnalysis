This is a programming assignment submitted as part of the Precog Research Group Recruitment Process.

The program uses the Twitter Streaming API to stream 10,000 tweets. Subsequently, it parses the tweets, performs Named Entity Recognition on them using the Natural Language Toolkit library and classifies them into negative/positive sentiment tweets. The tweets are then organized into a Pandas dataframe. Finally, the output is written to an excel sheet with the relevant fields. 

Requirements
	1. Python 2.7
	2. Numpy
	3. Scipy
	4. Python Twitter Tools
	5. Pandas
	6. NLTK
	7. Codecs (Python Library)
	8. Scikit-Learn

Most of the dependencies can be installed using a python package manager like pip.

Usage
The python scripts must be run in the following order:
	1. getTweets.py
	2. trainSentimentClassifier.py
	3. analyzeTweets.py

References
http://socialmedia-class.org/twittertutorial.html
http://adilmoujahid.com/posts/2014/07/twitter-analytics/
https://pythonprogramming.net/