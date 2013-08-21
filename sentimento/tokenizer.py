# -*- coding: utf-8 -*-
import re

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 
    'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 
    'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 
    'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 
    'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 
    'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
    'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',  
    'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 
    'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 
    'such', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 
    'very', 's', 't', 'can', 'will', 'just', 'should', 'now']

doubtful_stopwords = ['up', 'down', 'in', 'out', 'on', 'off', 
    'over', 'under', 'again']

negative_stopwords = ['not', 'no', 'isn\'t', 'isnt', 'dont', 'don\'t']

punctuation_regex = re.compile(r'^[^\w]{1}$')

# words_splitter = re.compile(r"[\w'<>@#]+|[.,!?;]")
words_splitter = re.compile(r"[\w'#@]+|[3<>:-D\)\(\|\\]{2,3}")

def tokenize(string):
    return [
        t.lower()
        for t in words_splitter.findall(string.rstrip())
        if len(t) > 0
    ]

def filter_stopwords(tokens):
    return [
        t
        for t in tokens
        if t not in stopwords
    ]

def filter_negative_stopwords(tokens):
    return [
        t
        for t in tokens
        if t not in negative_stopwords
    ]

def filter_punctuation(tokens):
    return [
        t
        for t in tokens
        if not punctuation_regex.match(t)
    ]

def filter_mentions(tokens):
    return [
        t
        for t in tokens
        if t[0] != '@'
    ]

def tags_to_words(tokens):
    f = lambda t: t[1:] if t[0] == '#' else t
    return [
        f(t)
        for t in tokens
    ]

def join_negations(tokens):

    caught_stopword = None
    grouped_tokenized = []
    for w in tokens:
        if w in negative_stopwords:
            caught_stopword = w
        else:
            if caught_stopword:
                grouped_tokenized.append('{} {}'.format(caught_stopword, w))
                caught_stopword = None
            else:
                grouped_tokenized.append(w)

    return grouped_tokenized


classic_filter_chain = (
    tokenize,
    filter_punctuation,
    filter_stopwords,
    filter_mentions,
    tags_to_words,
    join_negations
)
