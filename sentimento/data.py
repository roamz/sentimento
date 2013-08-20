# -*- coding: utf-8 -*-
import os.path

RT_DATA_DIR = os.path.abspath(
    os.path.join(*[
        os.path.dirname(__file__), 
        '..', 'data', 'rt', 'rt-polaritydata'
    ])
)

RT_CORPUS_FILE_POSITIVE = os.path.join(RT_DATA_DIR, 'rt-polarity-pos.txt')
RT_CORPUS_FILE_NEGATIVE = os.path.join(RT_DATA_DIR, 'rt-polarity-neg.txt')

BIASED_FILE_POSITIVE = os.path.join(RT_DATA_DIR, 'xtra-pos.txt')
BIASED_FILE_NEGATIVE = os.path.join(RT_DATA_DIR, 'xtra-neg.txt')

