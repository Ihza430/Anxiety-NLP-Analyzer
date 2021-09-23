import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Do you have anxiety?')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'EDA', 'Make a Prediction')
)

@st.cache
def load_data():
    df = pd.read_csv('../anx_writing.csv')
    return df

if page == 'About':
    st.subheader('About this project')
    st.write('''
    This is a Streamlit app that hosts my Poe vs. Austin model.
    
    The best model I found was a multinomial Naive Bayes classifier
    fit on count-vectorized text.
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