# main.py

from fastapi import FastAPI
import pandas as pd 

df = pd.read_csv('./data/Drugs2018.csv')

app = FastAPI()


@app.get('/')
def home():
    return 'this is an API service for NPR code details'

@app.get('/preview')
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.get('/npr/{value}')
def nprcode(value: str):
    print('value: ', value)
    filtered = df[df['NPROPNAME'] == value]
    if len(filtered) <= 0:
        return 'Not Available'
    else: 
        return filtered.to_json(orient="records")

@app.get('/icd/{value}/sex/{value2}')
def icdcode2(value: str, value2: str):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'Not Available'
    else: 
        return filtered2.to_json(orient="records")