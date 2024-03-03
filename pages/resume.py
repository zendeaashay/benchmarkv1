#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:46:35 2024

@author: aashayzende
"""

iimport streamlit as st

def show_resume():
    st.title('My Resume')

    # You can add more content here as needed
    st.write("Here is my resume showcasing my experience and skills.")

    # Link to download resume
    resume_link = 'path_to_resume.pdf'
    with open(resume_link, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="resume.pdf",
            mime="application/pdf"
        )

# Execute the function to display the resume
show_resume()