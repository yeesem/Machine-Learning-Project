import pandas as pd
import streamlit as st
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Prediction App

This app predicts the **Palmer Penguin** species
         
         """)

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example of CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

#Collects the user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input csv file",type=["csv"])