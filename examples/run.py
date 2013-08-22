# -*- coding: utf-8 -*-
import itertools
from sentimento.corpus import FileCorpusSource
from sentimento.algo import run_classic
from sentimento import data
from sentimento.regex import POSITIVE_EMOJI_FINDER, NEGATIVE_EMOJI_FINDER
import re

negative_emoji = re.compile(NEGATIVE_EMOJI_FINDER, flags=re.IGNORECASE)
positive_emoji = re.compile(POSITIVE_EMOJI_FINDER, flags=re.IGNORECASE)

def test_classic_rt():
    positive_training_corpus = itertools.chain(*[
        FileCorpusSource(data.RT_CORPUS_FILE_POSITIVE).entries(),
        FileCorpusSource(data.BIASED_FILE_POSITIVE).entries(),        
    ])
    negative_training_corpus = itertools.chain(*[
        FileCorpusSource(data.RT_CORPUS_FILE_NEGATIVE).entries(),
        FileCorpusSource(data.BIASED_FILE_NEGATIVE).entries(),        
    ])

    positive_test_corpus = FileCorpusSource(data.TEST_FILE_POSITIVE).entries()
    negative_test_corpus = FileCorpusSource(data.TEST_FILE_NEGATIVE).entries()

    run_classic(
        positive_training_corpus, 
        negative_training_corpus, 
        positive_test_corpus, 
        negative_test_corpus,
        verbose=False
    )

def filter_lines(gen, regex):
    return (
        e for
        e in gen
        if regex.findall(e)
    )

def test_classic_lm():
    train_pos = filter_lines(FileCorpusSource(data.LM_TRAIN_POSITIVE).entries(), positive_emoji)
    train_neg = filter_lines(FileCorpusSource(data.LM_TRAIN_NEGATIVE).entries(), negative_emoji)


    test_pos = filter_lines(FileCorpusSource(data.LM_TEST_POSITIVE).entries(), positive_emoji)
    test_neg = filter_lines(FileCorpusSource(data.LM_TEST_NEGATIVE).entries(), negative_emoji)

    run_classic(
        train_pos, 
        train_neg, 
        test_pos, 
        test_neg,
        verbose=False
    )

if __name__ == '__main__':
    test_classic_rt()
    test_classic_lm()