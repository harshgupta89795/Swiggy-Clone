import streamlit as st
import pandas as pd
import csv

filepath= "database/user_data.csv"
df1=pd.read_csv(filepath)
def sign_up():
    st.title("Welcome! Sign up to create account")
    with st.form(key="my_form"):
        name = st.text_input("Name",placeholder="Name")
        age = st.text_input("Age",placeholder="Age")
        city = st.text_input("City",placeholder="City")
        state = st.text_input("State",placeholder="State")
        pin = st.text_input("Pincode",placeholder="Pincode")
        user_email = st.text_input("Enter your email address",placeholder="Email")
        password = st.text_input("Enter your password",placeholder="Password")
        button = st.form_submit_button("Next")

    if button:
        if len(password) < 8:
            st.warning("Password should be of minimum  8 characters long")
        else:
            if user_email in df1['Email'].values:
                st.error("This email is already registered with us! Sign up with a different one.")
            else:
                with open("database/user_data.csv", 'a') as file:
                    writer1=csv.writer(file)
                    writer1.writerow([name,age,city,state,pin,user_email,password])
                st.success(f"Success!{name}")
sign_up()