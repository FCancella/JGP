from fastapi import FastAPI
import pandas as pd

# CPI All items, seasonally adjusted = CUSR0000SA0
# CPI All items, less food and energy, seasonally adjusted = CUSR0000SA0L1E
# CPI Gasoline (all types), seasonally adjusted = CUSR0000SETB01

app = FastAPI()

@app.get("/series/")
def read():
    available_series = {
        'CUSR0000SA0': 'CPI All items, seasonally adjusted',
        'CUSR0000SA0L1E': 'CPI All items, less food and energy, seasonally adjusted',
        'CUSR0000SETB01': 'CPI Gasoline (all types), seasonally adjusted'
    }
    return available_series

@app.get("/series/all/")
def read_data():
    df = pd.read_csv('cpi_data.csv')
    return df.to_dict(orient='records')

@app.get("/series/{series_id}/")
def read_data(series_id: str):
    df = pd.read_csv('cpi_data.csv')
    df = df[['date', series_id]]
    return df.to_dict(orient='records')