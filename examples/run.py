# -*- coding: utf-8 -*-
import itertools
from sentimento.classifier import NaiveBayesNLTKClassifier, \
    simple_nltk_feature_set_converter
from sentimento.corpus import FileCorpusSource
from sentimento import tokenizer
from sentimento import data

def apply_functions(arg, functions):
    return reduce(
        (lambda a, f: f(a)), 
        functions, 
        arg
    )

def run_rt_data():
    positive_corpus = itertools.chain(*[
        FileCorpusSource(data.RT_CORPUS_FILE_POSITIVE).entries(),
        FileCorpusSource(data.BIASED_FILE_POSITIVE).entries(),        
    ])
    negative_corpus = itertools.chain(*[
        FileCorpusSource(data.RT_CORPUS_FILE_NEGATIVE).entries(),
        FileCorpusSource(data.BIASED_FILE_NEGATIVE).entries(),        
    ])

    filter_chain = (
        tokenizer.tokenize,
        tokenizer.filter_punctuation,
        tokenizer.filter_stopwords,
        tokenizer.filter_mentions,
        tokenizer.tags_to_words,
        tokenizer.join_negations
    )
    positive_filter_chain = filter_chain + (
        simple_nltk_feature_set_converter('+'),
    )
    negative_filter_chain = filter_chain + (
        simple_nltk_feature_set_converter('-'),
    )

    positive_feature_sets = [
        apply_functions(e, positive_filter_chain)
        for e in positive_corpus
    ]

    negative_feature_sets = [
        apply_functions(e, negative_filter_chain)
        for e in negative_corpus
    ]

    classifier = NaiveBayesNLTKClassifier()
    classifier.train(positive_feature_sets + negative_feature_sets)

    tests = [
        'There is a cow chilling on the ceiling',
        'Never too cold for froyo <3 #wowcow #parramatta #rainydays #froyo',
        'Thanks commonwealth bank for fucking up my home loan!',
        'Sad that commonwealth bank ruined my home loan!',
        'dear qantas - answer your phone!!!!!!! ive been on hold for 2 hours!!!! bad service qantas!!! im over you :(',
        'I don\'t like it.',
        'I like it.',
        'That\'s not bad!',
        'That\'s not good!',
        'That\'s good!'
    ]

    test_feature_sets = [
        apply_functions(e, filter_chain)
        for e in tests
    ]

    for feature_set in test_feature_sets:
        print '{}: {}'.format(feature_set, classifier.classify({w:True for w in feature_set}))


if __name__ == '__main__':
    run_rt_data()