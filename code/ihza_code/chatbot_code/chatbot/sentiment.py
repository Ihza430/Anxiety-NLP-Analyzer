import pandas as pd
import numpy as np
import pickle

import emoji
import functools
import operator
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Instantiate Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

#Azin's code
def extract_emojis(s):
    """
    Extracts emojis from text.
    """
    return ''.join(c for c in s if c in emoji.UNICODE_EMOJI['en'])

def separate_emojis(em):
    """
    Separates emojis from each other.
    # https://stackoverflow.com/questions/49921720/how-to-split-emoji-from-each-other-python
    """
    em_split_emoji = emoji.get_emoji_regexp().split(em)
    em_split_whitespace = [substr.split() for substr in em_split_emoji]
    em_split = functools.reduce(operator.concat, em_split_whitespace)
    return ' '.join(em_split)

def get_emoji_scores(emtext, emoji_dict): 
    items = emtext.split()

    default = {'pos': 0, 'neu': 0, 'neg': 0, 'compound': 0}
    out = {'pos': 0, 'neu': 0, 'neg': 0, 'compound': 0}
    not_found = []
    for item in items:
        values = emoji_dict.get(item, default)
        if values == default:
            if item not in not_found:  
                t = emoji.demojize(item)
                text = t.replace('_', ' ').replace(':', '')
                values = analyzer.polarity_scores(text)
#                 print(item, text, values['compound'])
                not_found.append(item)  
        for k in default.keys():
            out[k] +=values[k]
    return out

def get_emoji_dict():
    emojis_path = './data/emoji_scores.csv'
  
    df = pd.read_csv(emojis_path)

    out = df[['emoji', 'neg', 'neu', 'pos', 'compound']]
    out.set_index('emoji', inplace=True)
    emoji_dict = out.to_dict(orient='index')
    return emoji_dict

def read_dict_pickle():
    path = './pickles/word_score.pkl'
    with open(path, 'rb') as pickle_in:
        word_dict = pickle.load(pickle_in)
    return word_dict

punc_dict = {'???': -1,'...': -0.3,'?!?!': -1.5,'!!!': -1}

def get_sentiment_score(text):
    emoji_dict = get_emoji_dict()
    
    word_dict = read_dict_pickle()
    
    analyzer.lexicon.update(emoji_dict)
    analyzer.lexicon.update(word_dict)
    analyzer.lexicon.update(punc_dict)

    vs = analyzer.polarity_scores(text)
    emtext = separate_emojis(extract_emojis(text))
    vs_em = get_emoji_scores(emtext, emoji_dict)
    
    for k, v in vs.items():
        vs[k] += vs_em[k]

    return vs['compound']