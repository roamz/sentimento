# -*- coding: utf-8 -*-
import nltk

def words_distribution(words):
    return nltk.FreqDist(words)


def subset_of_distribution(distribution, cutoff_factor=0.05):
    max = distribution[distribution.max()]
    cutoff = int(cutoff_factor * max)

    return [k for (k,v) in distribution.items() if v >= cutoff]
