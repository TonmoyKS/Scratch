# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:08:59 2024

@author: tonmo
"""
import streamlit as st 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="The Machine Learning App", layout='wide')