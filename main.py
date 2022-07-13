import streamlit as st
from passlib.hash import sha256_crypt
import yaml

Title = st.container()
Surname = st.container()
Name = st.container()
EmailAddress = st.container()
Group = st.container()
Need_for_laptop = st.container()
Keyboard_Configuration = st.container()
Password = st.container()


def main():

    with Title:
        st.title('Welcome to Heuritech')

    with Surname:
        surname = st.text_input("Enter you surname here")
        st.text("") # all of these empty st.text are to add space between the text inputs

    with Name:
        name = st.text_input("Enter your name here")
        st.text("")

    with EmailAddress:
        email = st.text_input("Enter your email address here")
        st.text("")

    with Group:
        group = st.text_input("Enter what group you are working with")
        st.text("")

    with Need_for_laptop:
        option1 = st.selectbox('What kind of laptop do you need?', ('Mac', 'PC', 'None'))
        st.write('You selected:', option1)
        st.text("")

    with Keyboard_Configuration:
        option2 = st.selectbox('What keyboard configuration do you need?', ('qwerty', 'azerty', 'none'))
        st.write('You selected:', option2)
        st.text("")

    with Password:
        st.subheader('Create your account password')
        user_input = st.text_input("Enter your password", type="password")
        user_input2 = st.text_input("Confirm your password", type="password")

        # Checks if passwords are matching
        if user_input == user_input2:
            st.caption("Passwords match")
        else:
            st.caption("Passwords do not match")

        st.text("")
        # Hashes the password
        password_hash = sha256_crypt.hash(user_input)

    # create  a yamlfile containing all user inputs, which is to be implemented into download_button

    dict_file = {'Form Contents': {'surname': surname,
                                   'name': name,
                                   'emai': email,
                                   'group': group,
                                   'option1': option1,
                                   'option2': option2,
                                   'password_hash': password_hash}}

    with open('test_yaml.yml', 'w') as file:
        yaml.dump(dict_file, file, sort_keys=False)


if __name__ == '__main__':
    main()
