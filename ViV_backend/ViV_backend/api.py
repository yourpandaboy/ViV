import pandas as pd
from fastapi import FastAPI
from ViV_backend.matcher import Matcher
import uvicorn
app = FastAPI()

@app.get("/")
def index():
    return {"ok":True}

@app.get("/get_bio")
def predict(bio):
    #call model + bio
    temp_matcher = Matcher(bio)
    return temp_matcher.top_matches().iloc[0,0]

@app.get("/name")
def get_name(name):
    return {"wait":f"your name is {name}"}

@app.get("/age")
def get_age(age):
    return {"wait":f"your age is {int(age)}"}

@app.get("/status")
def get_status(status):
    return {"wait":f"your status is {status}"}
