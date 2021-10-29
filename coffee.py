import plotly.express as px
import numpy as np
import csv

with open("coffee.csv") as data_file:
    df = csv.DictReader(data_file)
    fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours", color = "week")
    fig.show()

def get_data_source(data_path):
    coffee = []
    sleep = []
    with open(data_path) as data_csv:
        bruh = csv.DictReader(data_csv)
        for row in bruh:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {"x": coffee, "y": sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "coffee.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()