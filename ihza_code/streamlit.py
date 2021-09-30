import streamlit as st
import pickle
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import regex as re

st.set_page_config(
    page_title = 'Anxiety',
    page_icon='🙃',
    initial_sidebar_state='auto'
)

st.page_select = st.sidebar.selectbox(
    'Navigation',
    ('Home', 'About', 'EDA', 'Analyze Text', 'Chatbot')
)

@st.cache
def load_data():
    df = pd.read_csv('../../clean_datasets/anx_writing.csv')
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

if st.page_select == 'Home':
    st.title('Anxiety Analyzer')
    
elif st.page_select == 'About':
    st.title('About this project')
    st.write('''
    This is a Streamlit app that hosts a model to determine whether a text shows signs of anxiety.
    
    The model being used is Logistic Regression.
    ''')

elif st.page_select == 'EDA':
    df = load_data()
    st.table(df.sample(5))

elif st.page_select == 'Analyze Text':

    with open('models/anxiety_log.pkl', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    your_text = st.text_area('Please enter some text:', max_chars=500)

    anxiety = model.predict([your_text])[0]

    st.write(f'What does your writing tell about you:  {anxiety.title()}.')
    
    if anxiety.title() == 'Anxiety':
        st.write('Would you like to talk')
        
        option = st.selectbox('Answer', ('Yes', 'No'))
        
        if option == 'Yes':
            st.write('Navigate to Chatbot')
        
        elif option == 'No':
            st.write('Take care, friend')
            
elif st.page_select == 'Chatbot': 
    st.title('Chatbot')
       
        msg = st.text_input('Hello') 
        
        if msg != '':
            