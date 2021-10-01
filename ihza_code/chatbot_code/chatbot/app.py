from flask import Flask, render_template, jsonify, request, Response
import processor
import sentiment
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import regex as re

app = Flask(__name__)

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
        anxiety = log_model.predict([X_test])[0]
        return render_template('result.html', prediction = anxiety, model = 'Logistic Regression')
    
    elif user_input['fav_language'] == 'Multinomial Naive Bayes':
        mnb_model = pickle.load(open('models/grid_CountVectorizer_MultinomialNB.pkl', 'rb'))
        anxiety = mnb_model.predict([X_test])[0]
        
        if anxiety == 0:
            anxiety = 'Anxiety'
        elif anxiety == 1:
            anxiety = 'No Anxiety'
            
        return render_template('result.html', prediction = anxiety, model = 'Multinomial Naive Bayes')
    
    #score = sentiment.score(X_test)
        
    
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
