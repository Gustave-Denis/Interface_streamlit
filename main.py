import streamlit as st
from passlib.hash import sha256_crypt

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

        if user_input == user_input2:
            st.caption("Passwords match")
        else:
            st.caption("Passwords do not match")

        st.text("")

        submit = st.button('Press button to generate hashed password')
        st.text("")
        password_hash = sha256_crypt.hash(user_input)
        if submit:
            password_hash
        else:
            pass

    with open("content", "w+") as f:
        f.write(surname + "\n")
        f.write(name + "\n")
        f.write(email + "\n")
        f.write(group + "\n")
        f.write(option1 + "\n")
        f.write(option2 + "\n")
        f.write(password_hash)

    with open("content", "r") as f:
        st.download_button("Download form contents", f, "Heuritech.form.txt")


if __name__ == '__main__':
    main()
