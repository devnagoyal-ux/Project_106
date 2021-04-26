import csv
import numpy as np

def getDataSouce(data_path):
    marks  = []
    days = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
          marks .append(float(row["Marks In Percentage"]))
          days.append(float(row["Days Present"]))

    return {"x" : marks,"y" : days}

def find_corelation(datasource) :
    corelation  = np.corrcoef(datasource["x"],datasource["y"])
    print("Corelation b/w marks and  number of days is :- \n--->>",corelation[0,1])

def setup():
    data_path = "MarksVsDays.csv"
    datasource = getDataSouce(data_path)
    find_corelation(datasource)

setup()

import plotly.express as px
import pandas as pd
import csv

with open("MarksVsDays.csv") as csv_file:
    df = pd.read_csv(csv_file)
    fig =px.scatter(df,x = "Marks In Percentage", y = "Days Present", color="Roll No")
    fig.show()