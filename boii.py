import streamlit as st
import base64


# Set page config
st.set_page_config(page_title='Welcome to my page!', page_icon=':camera:', layout='wide')

# Main title
st.title("Home Page")

# Footer
st.markdown('---')
st.subheader('Aashay Zende')
st.caption('Data Wizard | Adventurer | Photographer | Surfer')

st.image('image.jpeg', caption='Exploring the Himalayas with my furry friends!')

# Introduction text with links to other pages
intro_text = """
Hey there! I'm Aashay, a data wizard by day and an adventurous spirit by... well, also by day (and sometimes night).
Currently weaving my magic with numbers and analytics at the prestigious D'Amore McKim School of Business, 
Northeastern University, I'm on a quest to make sense of the world, one dataset at a time. 
Born and raised in the bustling city of Mumbai, India, I've always been a bit of a nomad at heart, 
with my compass pointing towards icy mountain peaks and the soothing waves of beaches, [surfing](#).
I also love [painting](#) and [photography](#). Feel free to explore my other interests!
"""
st.markdown(intro_text)

# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:', 
                           ['Home', 'Resume', 'Photography', 'Surfing', 'Power BI Visualizations', 'ML Predictions', 'About'])

# Page content based on navigation choice
if options == 'Home':
    st.header('Home Page')
    st.write('Welcome to my world of adventures and analytics!')

from st_pages import Page, show_pages, add_page_title

def about_me():
    st.title('About Me')
    st.write('Here is some information about me...')

add_page_title()

show_pages([
    Page("home.py", "Home", "🏠"),
    Page(about_me, "About Me", "👤"),
    
])

