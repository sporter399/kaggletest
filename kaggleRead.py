import pandas as pd
import csv



trainDF = pd.read_csv('cs-test.csv')
trainDF.head()
trainDF.info()

print(trainDF)