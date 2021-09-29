import streamlit as st
import pickle
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import regex as re

st.set_page_config(
    page_title = 'Anxiety',
    page_icon='noto:upside-down-face',
    initial_sidebar_state='auto'
)

st.title('Do you have anxiety?')

page = st.sidebar.selectbox(
    'Navigation',
    ('About', 'EDA', 'Make a Prediction')
)

@st.cache
def load_data():
    df = pd.read_csv('../anx_writing.csv')
    return df


def custom_preprocessor (text):
    text = text.lower() #lowercases word
    text = re.sub(r'[^\w\s]', '', text) #removes punctuation
    text = re.sub(r'[0–9]', '', text) #removes any numbers
    text = re.sub('(<.*?>)', '', text) #removed html
    #copied from https://swatimeena989.medium.com/beginners-guide-for-preprocessing-text-data-f3156bec85ca

    lemmatizer = WordNetLemmatizer()
    text = lemmatizer.lemmatize(text)

    #p_stemmer = PorterStemmer()
    #text = p_stemmer.stem(text)

    return text
    #copied from https://www.studytonight.com/post/scikitlearn-countvectorizer-in-nlp

if page == 'About':
    st.subheader('About this project')
    st.write('''
    This is a Streamlit app that hosts a model to determine whether a text shows signs of anxiety.
    
    The model being used is Logistic Regression.
    ''')

elif page == 'EDA':
    df = load_data()
    st.table(df.sample(5))

elif page == 'Make a Prediction':

    with open('models/anxiety_log.pkl', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    your_text = st.text_input('Please enter some text:', max_chars=500)

    anxiety = model.predict([your_text])[0]

    st.write(f'What does your writing tell about you:  {anxiety.title()}.')
    
    if anxiety.title() == 'Anxiety':
        st.write('Would you like to talk')
        
        if st.button('Yes'):
            st.write('Why hello there, friend')
        
        if st.button('No'):
            st.write('Take care, friend')
       