import pandas as pd
from fastapi import FastAPI, Request
from ViV_backend.matcher import Matcher
import uvicorn
app = FastAPI()

@app.get("/")
def index():
    return {"ok":True}

#get new user info
@app.get("/new user bio")
def new_user(name,bio,age,status,pref_age_start,pref_age_end,pref_sex,pref_status):
    age = int(age)
    pref_age_end = int(pref_age_end)
    pref_age_start = int(pref_age_start)
    if age < 18:
        return 'Go back to your mama.'

    if pref_sex.lower() == 'male':
        pref_sex = 1
    pref_sex = 2

    temp_matcher = Matcher(bio).top_matches()

    filtered_df = temp_matcher[(temp_matcher['sex'] == pref_sex) & (temp_matcher['age'].between(pref_age_start,pref_age_end)) & (temp_matcher['status'] == pref_status.lower())]
    return filtered_df.to_dict(orient='dict')
# @app.get("/get_bio")
# def get_bio(bio):
#     #call model + bio
#     temp_matcher = Matcher(bio)
#     return temp_matcher.top_matches().to_dict(orient='dict')

# @app.get("/age")
# def get_age(age):
#     return {"wait":f"your age is {int(age)}"}

# @app.get("/status")
# def get_status(status):
#     return {"wait":f"your status is: {status.lower()}"}

# #get new user's preference
# @app.get("/prefered age")
# def prefered_age(start,finish):
#     return f"your prefered age: {int(start)}-{int(finish)}"

# @app.get("/prefered sex")
# def prefered_sex(sex):
#     return f"your prefered gender: {sex.lower()}"

# @app.get("/prefered status")
# def prefered_status(status):
#     return f"your prefered status: {status}"


# #implement the info with the model
# @app.get("/predict")
# def prediction():
#     temp_matcher = Matcher(bio)
#     return temp_matcher.top_matches().to_dict(orient='dict')
