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
    def __init__(self, threshold=0.7, undecided_label='neutral'):
        super(NaiveBayesNLTKClassifier, self).__init__()
        self.classifier = None
        self.threshold = threshold
        self.undecided_label = undecided_label

    def train(self, feature_sets):
        self.classifier = nltk.classify.NaiveBayesClassifier.train(
            feature_sets
        )
        self.classifier.show_most_informative_features(20)

    def classify(self, feature_set):
        classified = self.classifier.prob_classify({f:True for f in feature_set})
        result = {tag:classified.prob(tag) for tag in classified.samples()}

        decision = self.undecided_label
        for tag, value in result.items():
            if value >= self.threshold:
                decision = tag

        return {
            'decision': decision,
            'result': result
        }
        # return self.classifier.classify({f:True for f in feature_set})

