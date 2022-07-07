import streamlit as st
import hashlib

Title = st.container()
Surname = st.container()
Name = st.container()
EmailAddress = st.container()
Password = st.container()
Group = st.container()
Need_for_laptop = st.container()
Keyboard_Configuration = st.container()

with Title:
    st.title('Welcome to Heuritech')


with Surname:
    st.header('What is your surname?')
    user_input = st.text_input("Enter you surname here")


with Name:
    st.header('What is your name?')
    user_input2 = st.text_input("Enter your name here")


with EmailAddress:
    st.header('What is your email address?')
    user_input3 = st.text_input("Enter your email address here")


with Password:
    st.header('Create your password')
    user_input4 = st.text_input("Enter your password", type= "password")

    user_input5 = st.text_input("Confirm your password", type= "password")

    def make_hasher(user_input4, user_input5):
        return hashlib.sha256(str.encode(user_input4, user_input5)).hexdigest()

    if user_input4 == user_input5:
        st.caption("Passwords match")
    else:
        st.caption("Passwords do not match")


with Group:
    st.header('What group are you working with?')
    user_input6 = st.text_input("Enter what group you are working with")


with Need_for_laptop:
    st.header('What kind of laptop do you need?')
    option = st.selectbox('What kind of laptop do you need?', ('Mac', 'PC', 'None'))
    st.write('You selected:', option)

with Keyboard_Configuration:
    st.header('What keyboard Configuration do you need?')
    option = st.selectbox('What keyboard configuration do you need?', ('qwerty', 'azerty', 'none'))
    st.write('You selected:', option)