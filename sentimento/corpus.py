# -*- coding: utf-8 -*-

class CorpusSource(object):
    ''' Loads a list of tuples (<feature set>, label).
    In real life you should call 'read' that will return, say a tuple with 
    a list of words as the first argument and a label (positive/negative) as 
    the second one. 
    '''
    def entries(self):
        raise NotImplementedError()


class FileCorpusSource(CorpusSource):

    def __init__(self, filepath):
        super(FileCorpusSource, self).__init__()
        self.filepath = filepath

    def entries(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                yield line        
