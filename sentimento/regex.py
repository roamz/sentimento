# -*- coding: utf-8 -*-
import re

''' Text finder regexps are tailored to automatically classify text
using tags common in social networks.
'''

POSITIVE_EMOJI_FINDER = '|'.join([
    '[=:;8xB]-?[\)D3]', '<3'
])

NEGATIVE_EMOJI_FINDER = '|'.join([
    '[=:;8xB]-?[\(\|\\\]'
])

POSITIVE_TEXT_FINDER = '|'.join([
    '[=:;8xB]-?[\)D3]', '<3', 'amazing', 'w00t', 'fuckyea', 'shityea', 'lol'
])

NEGATIVE_TEXT_FINDER = '|'.join([
    '[=:;8xB]-?[\(\|\\\]', 'fail', 'sucks', 'wrong', 'ruin', 'screw'
])

if __name__ == '__main__':
    for t in [':)', ':D', '=)', '<3', 'LOL']:
        assert re.match(POSITIVE_TEXT_FINDER, t, re.IGNORECASE), '+ {}'.format(t)


    for t in [':(', ':(((', 'screw you']:
        assert re.match(NEGATIVE_TEXT_FINDER, t, re.IGNORECASE), '- {}'.format(t)
