import pandas as pd
import numpy as np
import csv
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
import sqlite3

trainDF = pd.read_csv('cs-test.csv')

engine = create_engine('sqlite://', echo=False)
trainDF.to_sql('applicants', con=engine)
engine.execute("SELECT * FROM applicants").fetchall()

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    output = trainDF.at[227, 'age']
    age_var = []

    for i in range(len(trainDF.index)):
        ret_age = trainDF.at[i, 'age']
        if ret_age < 50:
            age_var.append(ret_age)
        
        
    
    
    return render_template('base.html',output=output, age_var=age_var)

if __name__ == '__main__':
    app.run()