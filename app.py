from flask import Flask,render_template ,request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model=pickle.load(open('heart_disease.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        fbs = int(request.form['sugar'])
        if fbs>120:
            fbs=1
        else:
            fbs=0
        chol = int(request.form['cholestoral'])
        thal = int(request.form['thal'])
        trestbps = int(request.form['bp'])
        thalach = int(request.form['mhr'])
        slope = int(request.form['slope'])
        exang	 = int(request.form['exercise'])
        oldpeak = int(request.form['oldpeak'])
        ca = int(request.form['vessel'])
        restecg = int(request.form['electrocardiographic'])
        output=model.predict([[age,sex,cp,fbs,chol,thal,trestbps,thalach,slope,exang,oldpeak,ca,restecg]])
        print(output)
        if output==0:
            return render_template('prediction.html',prediction_text='You are safe you do not have any heart disease',param=output)
            
        else:
            return render_template('wrong.html',prediction_text='You are not safe you have heart disease')    
    return render_template("home.html")        
if __name__=="__main__":
    app.run(debug=True)    