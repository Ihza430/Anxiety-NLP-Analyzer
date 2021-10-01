"""
Modified from https://github.com/tatiblockchain/python-deep-learning-chatbot
Modified from Lesson 5.4
"""

# Libraries Used
from flask import Flask, render_template, jsonify, request, Response
import processor
import sentiment
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import regex as re

app = Flask(__name__)

# Needed to run Logistic model
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

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])

def anxiety_analyzer():
    user_input = request.args
    
    X_test = str(user_input['text'])
    
    if user_input['fav_language'] == 'Logistic Regression':
        log_model = pickle.load(open('models/anxiety_log.pkl', 'rb'))
        pred = log_model.predict([X_test])[0]
        
        if pred == 'Anxiety':
            score = sentiment.get_sentiment_score(X_test)
            
            if score < -0.85:
                pred = "Severe Anxiety"
            elif -0.85 < score < -0.25:
                pred = "Moderate Anxiety"
            elif -0.25 < score < 0.05:
                pred = "Mild Anxiety"
            else:
                pred = "No Anxiety"
            
        return render_template('result.html', prediction = pred, model = 'Logistic Regression')
    
    elif user_input['fav_language'] == 'Multinomial Naive Bayes':
        mnb_model = pickle.load(open('models/grid_CountVectorizer_MultinomialNB.pkl', 'rb'))
        pred = mnb_model.predict([X_test])[0]
        
        if pred == 0:
            score = sentiment.get_sentiment_score(X_test)
            
            if score < -0.85:
                pred = "Severe Anxiety"
            elif -0.85 < score < -0.25:
                pred = "Moderate Anxiety"
            elif -0.25 < score < 0:
                pred = "Mild Anxiety"
                
        elif pred == 1:
            pred = 'No Anxiety'
            
        return render_template('result.html', prediction = pred, model = 'Multinomial Naive Bayes')
        
    
@app.route('/messenger', methods=["GET", "POST"])
def messenger ():
    return render_template('chatbot.html', **locals())

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
