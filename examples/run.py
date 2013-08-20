# -*- coding: utf-8 -*-
import itertools
from sentimento.corpus import FileCorpusSource
from sentimento.algo import run_classic
from sentimento import data

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
        negative_test_corpus
    )

if __name__ == '__main__':
    test_classic_rt()