import pandas as pd
import numpy as np
import csv
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import os
from app import create_app

trainDF = pd.read_csv('cs-test.csv')

conn = sqlite3.connect('applicant_info.db')
c = conn.cursor()



c.execute('CREATE TABLE IF NOT EXISTS APPLICANTS (SeriousDlqin2yrs number,RevolvingUtilizationOfUnsecuredLines float, age number,NumberOfTime30to59DaysPastDueNotWorse number,DebtRatio float,MonthlyIncome number,NumberOfOpenCreditLinesAndLoans number,NumberOfTimes90DaysLate number,NumberRealEstateLoansOrLines number,NumberOfTime60to89DaysPastDueNotWorse number,NumberOfDependents number)')
conn.commit()
Applicants = trainDF

trainDF = DataFrame(Applicants, columns= ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30to59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines', 'NumberOfTime60to89DaysPastDueNotWorse', 'NumberOfDependents'])
trainDF.to_sql('APPLICANTS', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM APPLICANTS
        ''')


app = Flask(__name__)



sql_age = []
c.execute("SELECT age FROM APPLICANTS;")
result = c.fetchall()

ints_only = [item[0] for item in result] 

for i in range(len(ints_only)):
        
    test_var = int(ints_only[i])
        
    if test_var < 24:
        sql_age.append(test_var)
    

def add_vue_routes(app):
    @app.route('/')
    def serve_vue_app():
        print("line 51 in kaggleRead")
        """
        Server our vue app
        """
        return(render_template('base.html'))


    @app.after_request
    def add_header(req):
        """
        Clear Cache for hot-reloading
        """
        req.headers["Cache-Control"] = "no-cache"
        return req 

@app.route('/', methods=['POST', 'GET'])
def index():

    
    return render_template('base.html', sql_age=sql_age)

if __name__ == '__main__':
    app = create_app()
    add_vue_routes(app)
    
    app.run(debug=True)