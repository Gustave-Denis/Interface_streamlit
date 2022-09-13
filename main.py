import streamlit as st
from passlib.hash import sha256_crypt
import yaml

# Faut recuperer les données en temps que variables d'environement!
# need to save the form inputs as environmental variables in order to extract them using os.getenv/os.environ.get

Title = st.container()
Surname = st.container()
Name = st.container()
EmailAddress = st.container()
Group = st.container()
Need_for_laptop = st.container()
Keyboard_Configuration = st.container()
Password = st.container()


# Create form components
def main():

    with Title:
        st.title('Welcome to Heuritech')

    with Surname:
        surname = st.text_input("Enter you surname here")
        st.text("")  # all of these empty st.text are to add space between the text inputs

    with Name:
        name = st.text_input("Enter your name here")
        st.text("")

    with EmailAddress:
        email = st.text_input("Enter your email address here")
        st.text("")

    with Group:
        group = st.selectbox("What group you are working with", ('Infrastructure', 'Core', 'Product'))
        st.write('You selected:', group)
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
        sha256_crypt.verify(user_input, password_hash)

    # creates  a yaml file containing all user inputs once the submit button has been pressed.
    submit = st.button('Submit and Send')
    if submit:
        dict_file = {'Form Contents': {'surname': surname,
                                       'name': name,
                                       'email': email,
                                       'group': group,
                                       'laptop': option1,
                                       'keyboard configuration': option2,
                                       'password_hash': password_hash}}

        with open('test_yaml.yml', 'w') as file:
            yaml.dump(dict_file, file, sort_keys=False)

        exec(open("email.test.py").read())

        st.write(""
                 "Thank you, your form has been submitted")


if __name__ == '__main__':
    main()

