# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title('Benchmarks App')

st.write('Here you can see my Power BI visualizations and ML predictions.')

st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:', 
                           ['Home', 'Power BI Visualizations', 'ML Predictions', 'About'])

# Conditional rendering based on navigation choice
if options == 'Home':
    st.title('Home Page')
    st.write('Welcome to my Streamlit App!')

elif options == 'Power BI Visualizations':
    st.title('Power BI Visualizations')
    # Embed your Power BI Dashboard here
    # ...

elif options == 'ML Predictions':
    st.title('ML Predictions')
    # Add your ML prediction code here
    # ...

elif options == 'About':
    st.title('About')
    st.write('This is a Streamlit app demonstrating a multi-page navigation system.')