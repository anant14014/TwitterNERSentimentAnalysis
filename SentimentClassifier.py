#File: sentiment_mod.py

import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



class VotedSentimentClassifier(ClassifierI):
    def __init__(self, classifiers=None, word_features=None):
        if not classifiers:
            open_file = open("pickled_algos/originalnaivebayes5k.pickle", "rb")
            classifier = pickle.load(open_file)
            open_file.close()


            open_file = open("pickled_algos/MNB_classifier5k.pickle", "rb")
            MNB_classifier = pickle.load(open_file)
            open_file.close()

            open_file = open("pickled_algos/BernoulliNB_classifier5k.pickle", "rb")
            BernoulliNB_classifier = pickle.load(open_file)
            open_file.close()


            open_file = open("pickled_algos/LogisticRegression_classifier5k.pickle", "rb")
            LogisticRegression_classifier = pickle.load(open_file)
            open_file.close()


            open_file = open("pickled_algos/LinearSVC_classifier5k.pickle", "rb")
            LinearSVC_classifier = pickle.load(open_file)
            open_file.close()


            open_file = open("pickled_algos/SGDC_classifier5k.pickle", "rb")
            SGDC_classifier = pickle.load(open_file)
            open_file.close()

            classifiers = (classifier, LinearSVC_classifier, MNB_classifier, BernoulliNB_classifier, LogisticRegression_classifier)

        self._classifiers = classifiers

        if not word_features:
            open_file = open("pickled_algos/word_features5k.pickle", "rb")
            word_features = pickle.load(open_file)
            open_file.close()

        self._word_features = word_features

    def classify(self, text):
        features = self.find_features(text)
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / float(len(votes))
        return (mode(votes), conf)

    def find_features(self, text):
        words = word_tokenize(text)
        features = {}
        for w in self._word_features:
            features[w] = (w in words)
        return features