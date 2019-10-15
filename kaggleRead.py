import pandas as pd
import numpy as np
import csv
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import os
import sqlite3

trainDF = pd.read_csv('cs-test.csv')

conn = sqlite3.connect('applicant_info.db')
c = conn.cursor()
c.execute('CREATE TABLE APPLICANTS (SeriousDlqin2yrs number,RevolvingUtilizationOfUnsecuredLines float, age number,NumberOfTime30to59DaysPastDueNotWorse number,DebtRatio float,MonthlyIncome number,NumberOfOpenCreditLinesAndLoans number,NumberOfTimes90DaysLate number,NumberRealEstateLoansOrLines number,NumberOfTime60to89DaysPastDueNotWorse number,NumberOfDependents number)')
conn.commit()
Applicants = trainDF

trainDF = DataFrame(Applicants, columns= ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30to59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines', 'NumberOfTime60to89DaysPastDueNotWorse', 'NumberOfDependents'])
trainDF.to_sql('APPLICANTS', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM APPLICANTS
          ''')



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