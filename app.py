import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

##Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api', methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(np.array(list(data.values())).reshape(1,-1))
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])

def predict():
    data = [float(x) for x in request.form.values()]
    output = model.predict(np.array((data)).reshape(1,-1))[0]
    return render_template('home.html', prediction_text = 'The predicted house price is {}'.format(output))



if __name__=="__main__":
    app.run(debug=True)    
