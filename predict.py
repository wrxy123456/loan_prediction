import pickle
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

model = pickle.load(open('rfmodel.p','rb'))
cols = pickle.load(open('columns.p','rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method== 'POST':
        inp = []
        inp.append(request.form['gender'])
        inp.append(request.form['married'])
        inp.append(request.form['dependents'])
        inp.append(request.form['education'])
        inp.append(request.form['self_emp'])
        inp.append(int(request.form['loan_amt']))
        inp.append(int(request.form['loan_term']))
        inp.append(int(request.form['credit']))
        inp.append(request.form['area'])
        inp.append(int(request.form['app_inc'])+int(request.form['coapp_inc']))
        
        val = pd.DataFrame([inp],columns=cols)
        
        result = model.predict(val)
        if(result==1):
            return render_template('index.html',out='Approved')
        else:
            return render_template('index.html',out='Not Approved')

if __name__ == '__main__':
    app.run(debug=True, port='5555',host='0.0.0.0')