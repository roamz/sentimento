# -*- coding: utf-8 -*-
import os.path

DATA_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        '..', 'data'
    )
)


RT_DATA_DIR = os.path.abspath(
    os.path.join(
        DATA_DIR, 'rt', 'rt-polaritydata'
    )
)

RT_CORPUS_FILE_POSITIVE = os.path.join(RT_DATA_DIR, 'rt-polarity-pos.txt')
RT_CORPUS_FILE_NEGATIVE = os.path.join(RT_DATA_DIR, 'rt-polarity-neg.txt')

BIASED_FILE_POSITIVE = os.path.join(RT_DATA_DIR, 'xtra-pos.txt')
BIASED_FILE_NEGATIVE = os.path.join(RT_DATA_DIR, 'xtra-neg.txt')

TEST_FILE_POSITIVE = os.path.join(DATA_DIR, 'test', 'test_set_pos.txt')
TEST_FILE_NEGATIVE = os.path.join(DATA_DIR, 'test', 'test_set_neg.txt')
