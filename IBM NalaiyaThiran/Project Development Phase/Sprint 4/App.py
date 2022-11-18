

import numpy as np
import pickle
import joblib
import  matplotlib
import matplotlib.pyplot as plt
import time
import pandas
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open(r'C:\Users\Sreshta B\OneDrive\Desktop\Project Rainfall\model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=["POST","GET"])
def predict():
    input_features=[x for x in request.form.values() ]
    features_values=[np.array(input_features)]
    
    names = [['Location','MinTemp','MaxTemp','Rainfall','WindGustSpeed',
              'WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm',
              'Pressure9am','Pressure3pm','Temp9am','Temp3pm','RainToday',
              'WindGustDir','WindDir9am','WindDir3pm','year','month','day']]
    print(features_values)
    print(len(features_values))
    data = pandas.DataFrame(features_values,columns=names)
    
    
    
    prediction=model.predict(data)
    print(prediction)
    if prediction == "Yes":
        return render_template("chance.html")
    else:
        return render_template("nochance.html")
    
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
