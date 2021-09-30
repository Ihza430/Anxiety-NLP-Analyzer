from flask import Flask, render_template, jsonify, request, Response
import processor
import sentiment
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import regex as re

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])

def anxiety_analyzer():
    user_input = request.args
    
    X_test = str(user_input['text'])
    
    if user_input
    log_model = pickle.load(open('models/anxiety_log.pkl', 'rb'))
    anxiety = log_model.predict([X_test])[0]
    
    score = sentiment.score(X_test)
    
    return render_template('result.html', prediction = score)
   
        
    
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
