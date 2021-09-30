import pandas as pd
import numpy as np
import pickle

from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Instantiate Sentiment Analyzer
vader = SentimentIntensityAnalyzer()

words = pickle.load(open('./pickles/word_score.pkl','rb'))

vader.lexicon.update(words)

def score(text):
    score = vader.polarity_scores(str(text))
    
    if score['compound'] < -0.75:
        return "Severe Anxiety"
    
    elif -0.75 < score ['compound']< -0.25:
        return "Moderate Anxiety"
    
    elif -0.25 < score['compound'] < 0:
        return "Mild Anxiety"
    
    else: 
        return "No Anxiety"
    
def get_emoji_dict():
    emojis_path = '../data/emoji_scores.csv'
    if running_in_drive:
        emojis_path = '/content/drive/MyDrive/GA/data/emoji_scores.csv'


    df = pd.read_csv(emojis_path)

    out = df[['emoji', 'neg', 'neu', 'pos', 'compound']]
    out.set_index('emoji', inplace=True)
    emoji_dict = out.to_dict(orient='index')
    return emoji_dict

