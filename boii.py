# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

# Set page config
st.set_page_config(page_title='Aashay Zende', page_icon=':camera:', layout='wide')

# Main title
st.title('Aashay Zende\'s Portfolio')

st.write('Hey there! I\'m Aashay, a data wizard by day and an adventurous spirit by... well, also by day (and sometimes night).')

# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:', 
                           ['Home', 'Resume', 'Photography', 'Surfing', 'Power BI Visualizations', 'ML Predictions', 'About'])

# Page content based on navigation choice
if options == 'Home':
    st.header('Home Page')
    st.write('Welcome to my world of adventures and analytics!')
    st.image('image.jpeg', caption='Exploring the mountains with furry friends!')

elif options == 'Resume':
    st.header('Resume')
    # Here you could potentially use st.file_uploader and then display your resume PDF
    # Or use markdown to display your resume textually
    # ...

elif options == 'Photography':
    st.header('Photography')
    # Here you could use st.image to display your photographs
    # ...

elif options == 'Surfing':
    st.header('Surfing')
    # Similar to photography, you can display surfing images or videos
    # ...

elif options == 'Power BI Visualizations':
    st.header('Power BI Visualizations')
    # Embed your Power BI Dashboard here
    # ...

elif options == 'ML Predictions':
    st.header('ML Predictions')
    # Add your ML prediction code here
    # ...

elif options == 'About':
    st.header('About')
    st.write('This is a page about me and my Streamlit app.')

# Footer
st.markdown('---')
st.subheader('Aashay Zende')
st.caption('Data Wizard | Adventurer | Photographer | Surfer')