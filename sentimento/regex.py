# -*- coding: utf-8 -*-
import re

POSITIVE_TEXT_FINDER = '|'.join([
    '[=:;]-?[\)D3]', '<3', 'amazing', 'w00t', 'lol', 'rofl'
])

NEGATIVE_TEXT_FINDER = '|'.join([
    '[=:;]-?[\(\|\\\]', 'fail', 'fuck', 'shit', 'sucks', 
    'wrong', 'ruin', 'screw'
])

if __name__ == '__main__':
    for t in [':)', ':D', '=)', '<3', 'LOL']:
        assert re.match(POSITIVE_TEXT_FINDER, t, re.IGNORECASE), '+ {}'.format(t)


    for t in [':(', ':(((', 'SHIT', 'Fucked UP', 'screw you']:
        assert re.match(NEGATIVE_TEXT_FINDER, t, re.IGNORECASE), '- {}'.format(t)
