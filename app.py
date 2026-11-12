import flask
import  numpy as np
from flask import Flask,render_template,request
import pickle
import warnings
warnings.filterwarnings("ignore")
app=Flask(__name__)
with open("Model.pkl","rb") as p:
    m=pickle.load(p)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=['GET','POST'])
def predict():
    values=[float(i) for i in request.form.values()]
    r=m.predict([values])
    return render_template("index.html",prediction=float(r[0]))
if __name__=="__main__":
    app.run(debug=True)