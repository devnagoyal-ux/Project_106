import csv
import numpy as np

def getDataSouce(data_path):
    coffee  = []
    sleep = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
          coffee .append(float(row["Coffee in ml"]))
          sleep.append(float(row["sleep in hours"]))

    return {"x" : coffee,"y" : sleep}

def find_corelation(datasource) :
    corelation  = np.corrcoef(datasource["x"],datasource["y"])
    print("Corelation b/w coffee and  number of hours is :- \n--->>",corelation[0,1])

def setup():
    data_path = "CofeeVsSleep.csv"
    datasource = getDataSouce(data_path)
    find_corelation(datasource)

setup()

import plotly.express as px
import pandas as pd
import csv

with open("CofeeVsSleep.csv") as csv_file:
    df = pd.read_csv(csv_file)
    fig =px.scatter(df,x = "Coffee in ml", y = "sleep in hours", color="week")
    fig.show()