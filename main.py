import streamlit as st

Title = st.container()
Surname = st.container()
Name = st.container()
EmailAddress = st.container()

with Title:
    st.title('Welcome')


with Surname:
    st.header('What is your surname?')
    user_input = st.text_input("Enter you surname here")


with Name:
    st.header('What is your name?')
    user_input2 = st.text_input("Enter your name here")


with EmailAddress:
    st.header('What is your email address?')
    user_input = st.text_input("Enter your email address here")



