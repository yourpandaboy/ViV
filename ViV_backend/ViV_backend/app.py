from hashlib import new
from tkinter import N
import pandas as pd
import streamlit as st
from ViV_backend.matcher import Matcher

st.title("ViV")
st.header("Vibe, Interact, Live!")
st.write("Using Machine Learning to Find the Top Dating Profiles for you")

# Instantiating a new user DF
new_profile = pd.DataFrame(columns=['Name','Bio','Age','Status','Sex','Location']
                           )
# Asking for new profile data
name = st.text_input("Enter your name: ")
bio = st.text_input("Enter a Bio for yourself: ")
age = st.slider("What is your age?", 18, 70)
status = st.selectbox(
'Choose your relationship status',
('--','Single', 'In a relationship', 'Married'))
sex = st.selectbox(
'Choose your gender',
('--','Male', 'Female', 'Others'))
location = st.text_input("Enter your location: ")

new_profile_dict = {'Name':[name],
                    'Bio':[bio],
                    'Age':[age],
                    'Status':[status],
                    'Sex':[sex],
                    'Location':[location]}

new_profile = new_profile_dict
st.write(pd.DataFrame(new_profile))

# Instantiating a new user preference DF to use as a filter later
preference_df = pd.DataFrame(columns= ['Age_start','Age_end','Status','Sex'])

st.header("Tell ViV your preference!")

a,b = st.slider(
     'Prefered ages',
     18, 70, (18, 25))

st.write('Your prefered ages:', a)
st.write('Your prefered ages:', b)

c = st.selectbox(
'Your prefered status you want to meet',
('--','Single', 'In a relationship', 'Married'))

d = st.selectbox(
'Your prefered gender you want to meet',
('--','Male', 'Female', 'Others'))

preference_dict = {'Age_start': [a],
                   'Age_end':[b],
                   'Status':[c],
                   'Sex':[d]}

preference_df= a,b,c,d

st.write(pd.DataFrame(preference_dict))

matches = Matcher(bio).top_matches()
st.write(matches)
st.write(matches.shape)
st.button('finished')
