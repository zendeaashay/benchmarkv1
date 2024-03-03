import streamlit as st

# Set page configuration
st.set_page_config(page_title='Welcome to my page!', page_icon=':camera:', layout='wide')

# Main title and footer
st.title("Home Page")
st.markdown('---')
st.subheader('Aashay Zende')
st.caption('Data Wizard | Adventurer | Photographer | Surfer')

# Introduction text
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

# Function definitions for different pages
def home_page():
    st.header('Home Page')
    st.write('Welcome to my world of adventures and analytics!')
    st.image('image.jpeg', caption='Exploring the Himalayas with my furry friends!')  # Display the image

def resume_page():
    st.header('Resume')
    st.write("Here's my resume...")

def photography_page():
    st.header('Photography')
    st.write("Here's my photography portfolio...")

def surfing_page():
    st.header('Surfing')
    st.write("Here's my surfing adventures...")

def power_bi_page():
    st.header('Power BI Visualizations')
    st.write("Here are my Power BI visualizations...")

def ml_predictions_page():
    st.header('ML Predictions')
    st.write("Here are my machine learning predictions...")

def about_page():
    st.header('About Me')
    st.write("Here's some information about me...")

# Page content based on navigation choice
if options == 'Home':
    home_page()
elif options == 'Resume':
    resume_page()
elif options == 'Photography':
    photography_page()
elif options == 'Surfing':
    surfing_page()
elif options == 'Power BI Visualizations':
    power_bi_page()
elif options == 'ML Predictions':
    ml_predictions_page()
elif options == 'About':
    about_page()