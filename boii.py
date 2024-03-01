# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title('Benchmarks App')

st.write('Here you can see my Power BI visualizations and ML predictions.')
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)