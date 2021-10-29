import plotly.express as px
import numpy as np
import csv

with open("marks.csv") as data_file:
    df = csv.DictReader(data_file)
    fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present", color = "Roll No")
    fig.show()

def get_data_source(data_path):
    percentage = []
    days = []
    with open(data_path) as data_csv:
        bro = csv.DictReader(data_csv)
        for row in bro:
            percentage.append(float(row['Marks In Percentage']))
            average.append(float(row['Days Present']))
    return {"x": percentage, "y": days}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "marks.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()