#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:46:35 2024

@author: aashayzende
"""

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def show_resume():
    st.title('My Resume')

    # You can add more content here as needed
    st.write("Here is my resume showcasing my experience and skills.")

    # Display the resume PDF
    pdf_viewer("Aashay Zende - Resume.pdf", width=700, height=1000)

# Execute the function to display the resume
show_resume()

    # You can add more content here as needed
    st.write("Here is my resume showcasing my experience and skills.")

    # Link to download resume
    resume_link = 'Aashay Zende - Resume.pdf'
    with open(resume_link, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Aashay Zende - Resume.pdf",
            mime="application/pdf"
        )

# Execute the function to display the resume
show_resume()