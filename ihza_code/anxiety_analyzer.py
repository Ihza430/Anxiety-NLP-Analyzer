#imports
import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, jsonify, request
import processor


# initialize the flask app
app = Flask('Anxiety Analyzer')

#route 1: Home
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

#route 2: Chatbot
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        
        response = processor.chatbot_response(the_question)
    return jsonify({"response": response })

#route 3: Text Analyzer
@app.route('/text_analyzer')
def away():
    return "do something"



# Call app.run(debug=True) when python script is called
if __name__ == '__main__':
    app.run(debug = True)