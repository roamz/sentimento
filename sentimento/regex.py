# -*- coding: utf-8 -*-

POSITIVE_TEXT_FINDER = '|'.join([
    '[=\:\;]-?[\)D]', '<3', 'amazing', 'w00t'
])

NEGATIVE_TEXT_FINDER = '|'.join([
    '[=\:;]-?[\(\|\\]', 'fail', 'fuck[^ing]', 'shit', 'sucks', 'wrong', 'ruin'
])
