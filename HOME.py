import streamlit as st

# Set page title and icon
st.set_page_config(page_title='SSB Yodha', page_icon='✊')

# Front Page Title
st.title('Welcome to SSB Yodha')

# Introduction Section
st.header('About SSB Yodha')
ssb_description = """
SSB Yodha is your ultimate guide to cracking the Service Selection Board (SSB) exam and fulfilling your dream of joining the military. 
Our comprehensive resources and expert guidance will prepare you for each stage of the SSB selection process, ensuring your success in the 
interviews and examinations.
"""
st.markdown(ssb_description)

# SSB Exam Process Section
st.header('SSB Exam Process')
exam_process = """
The SSB exam consists of multiple stages including Screening Test, Psychological Testing, Group Testing, Interview, and Medical Examination. 
Each stage evaluates different aspects of a candidate's suitability for the military. At SSB Yodha, we provide detailed insights, practice 
materials, and tips for each stage to help you excel in the selection process.
"""
st.markdown(exam_process)

# How SSB Yodha Helps Section
st.header('How SSB Yodha Helps You')
help_description = """
SSB Yodha offers personalized coaching, mock interviews, and interactive sessions to enhance your skills. Our experienced mentors provide 
guidance on leadership, communication, and psychological aspects, ensuring you are well-prepared for the challenges of the SSB exam. 
Join SSB Yodha today and embark on your journey to becoming a military officer!
"""
st.markdown(help_description)


