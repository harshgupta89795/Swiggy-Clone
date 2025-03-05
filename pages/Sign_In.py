import streamlit as st
import pandas as pd

# Load user data
df1 = pd.read_csv("database/user_data.csv")

# Initialize session state variables
if "signed_in_user" not in st.session_state:
    st.session_state["signed_in_user"] = None

if "current_page" not in st.session_state:
    st.session_state["current_page"]="Sign_In.py"

# Sign-in function
def sign_in():
    st.title("Welcome! Sign in to your account")
    with st.form(key="sign"):
        user_email = st.text_input("Email", placeholder="Email")
        passcode = st.text_input("Password", placeholder="Password", type="password")
        butt = st.form_submit_button("Sign in")
        if butt:
            found = False
            for index, row in df1.iterrows():
                if row["Email"] == user_email:
                    if row["Password"] == passcode:
                        found = True
                        st.session_state["signed_in_user"] = row.to_dict()
                        st.success("Success")
                        st.rerun()
                    else:
                        st.error("Invalid email or password. Please try again.")
                        break
            if not found:
                st.error("Entered email is not registered with us! Please sign up first.")

def profile_page():
    user=st.session_state['signed_in_user']
    st.title("Your Profile")
    st.subheader("Profile Details")
    st.write(f"**Name:** {user['Name']}")
    st.write(f"**Email:** {user['Email']}")
    st.write(f"**Age:** {user['Age']}")
    st.write(f"**City:** {user['City']}")
    st.write(f"**State:** {user['State']}")
    st.write(f"**Pincode:** {user['Pincode']}")
    st.sidebar.header(user['Name'])
    if st.button("Goto Home Page"):
        st.session_state["current_page"]="About.py"
        st.rerun()
    if st.session_state["current_page"]=="About.py":
        from pages import About
        About.render()
    if st.button("Log out"):
        st.session_state["signed_in_user"] = None
        st.rerun()

if st.session_state["signed_in_user"] is not None:
    profile_page()
else:
    sign_in()
