# -*- coding: utf-8 -*-
import nltk.classify

def simple_nltk_feature_set_converter(label):
    def converter(tokens):
        return (
            {t: True for t in tokens},
            label
        )
    return converter


class Classifier(object):
    def train(self, feature_sets):
        raise NotImplementedError()

    def classify(self, features):
        raise NotImplementedError()


class NaiveBayesNLTKClassifier(object):
    def __init__(self):
        super(NaiveBayesNLTKClassifier, self).__init__()
        self.classifier = None

    def train(self, feature_sets):
        self.classifier = nltk.classify.NaiveBayesClassifier.train(
            feature_sets
        )
        self.classifier.show_most_informative_features(20)

    def classify(self, features):
        return self.classifier.classify(features)

