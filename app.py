import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

## creating a Flask app
app = Flask(__name__)

##Load the model
model = pickle.load(open('model.pkl', 'rb'))

## routing the flask app to home.html page which has a simple front end to input values for user
@app.route('/')
def home():
    return render_template('home.html') # render_template will look for template folder where home.html file is present

## using this predict_api we are requesting data as a json file and then using pickle to predict the output
## here POST means that this predict_api is looking for some data in json format from client side 
## so it will not work directly you have to use postman to give data and then it will predict results
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(np.array(list(data.values())).reshape(1,-1))
    print(output[0])
    return jsonify(output[0])


## using this predict now we are taking input from a form which is actually taking input from an HTML page
## the complete process is when we run app.py it will open an html page
##  in html code wehave defined a predict which will use this api and predict using inputs given in HTML
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    output = model.predict(np.array(data).reshape(1,-1))[0]
    return render_template('home.html', prediction_text = 'The predicted house price is {}'.format(output))


## used to run the flask app in debug mode
if __name__=="__main__":
    app.run(debug=True)    
