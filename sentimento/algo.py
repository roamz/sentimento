# -*- coding: utf-8 -*-
from . import tokenizer
from sentimento.classifier import NaiveBayesNLTKClassifier, \
    simple_nltk_feature_set_converter

LABEL_POSITIVE = '+'
LABEL_NEGATIVE = '-'

def apply_functions(arg, functions):
    return reduce(
        (lambda a, f: f(a)), 
        functions, 
        arg
    )


def run_classic(positive_training_corpus, 
    negative_training_corpus, positive_test_corpus,
    negative_test_corpus):

    filter_chain = (
        tokenizer.tokenize,
        tokenizer.filter_punctuation,
        tokenizer.filter_stopwords,
        tokenizer.filter_mentions,
        tokenizer.tags_to_words,
        tokenizer.join_negations
    )
    positive_filter_chain = filter_chain + (
        simple_nltk_feature_set_converter(LABEL_POSITIVE),
    )
    negative_filter_chain = filter_chain + (
        simple_nltk_feature_set_converter(LABEL_NEGATIVE),
    )

    print('Loading training data...')

    positive_feature_sets = [
        apply_functions(e, positive_filter_chain)
        for e in positive_training_corpus
    ]

    negative_feature_sets = [
        apply_functions(e, negative_filter_chain)
        for e in negative_training_corpus
    ]

    classifier = NaiveBayesNLTKClassifier()
    print('Training...')
    classifier.train(positive_feature_sets + negative_feature_sets)
    print('Done!')

    test_corpuses = [
        (LABEL_POSITIVE, positive_test_corpus),
        (LABEL_NEGATIVE, negative_test_corpus)
    ]

    for label, corpus in test_corpuses:
        test_feature_sets = [
            apply_functions(line, filter_chain)
            for line in corpus
        ]

        print('Testing "{}"'.format(label))
        print('--------')
        for feature_set in test_feature_sets:
            result = classifier.classify(feature_set)
            print '{}: {}'.format(feature_set, result)
        print('')
