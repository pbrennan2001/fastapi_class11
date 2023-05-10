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

@app.get("/npr/{npr_code}")
def search_by_npr_code(npr_code: str):
    data = df.loc[df['NPR_CODE'] == npr_code].to_dict(orient='records')
    if len(data) == 0:
        return {"message": "No data found for NPR code {}".format(npr_code)}
    else:
        return data

@app.get("/drugname/{drug_name}")
def search_by_drug_name(drug_name: str):
    data = df.loc[df['DRUG_NAME'] == drug_name].to_dict(orient='records')
    if len(data) == 0:
        return {"message": "No data found for drug {}".format(drug_name)}
    else:
        return data