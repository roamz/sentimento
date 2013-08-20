# -*- coding: utf-8 -*-

POSITIVE_TEXT_FINDER = '|'.join([
    '[=\:\;]-?[\)D3]', '<3', 'amazing', 'w00t', 'lol', 'rofl'
])

NEGATIVE_TEXT_FINDER = '|'.join([
    '[=\:;]-?[\(\|\\]', 'fail', 'fuck[^ing] (up)?', 'shit', 'sucks', 
    'wrong', 'ruin', 'screw'
])
