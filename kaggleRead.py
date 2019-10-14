import pandas as pd
import csv
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3



trainDF = pd.read_csv('cs-test.csv')

trainDF.head()

app = Flask(__name__)





@app.route('/rawdata', methods=['POST', 'GET'])
def raw_data():

    raw_array = []
    raw_array.append(trainDF)
    print("line 25 in python")
    
    return render_template('rawdata.html',raw_array=raw_array)


@app.route('/', methods=['POST', 'GET'])
def index():


    raw_array = []
    raw_array.append(trainDF)
    print("raw_array in python code    " + str(raw_array))
    print("line 33 in python")
    
    return render_template('base.html',len = len(raw_array),raw_array=raw_array)




##print(trainDF)

if __name__ == '__main__':
    app.run()