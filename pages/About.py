import streamlit as st

if "signed_in_user" not in st.session_state:
    st.session_state["signed_in_user"] = None

if "current_page" not in st.session_state:
    st.session_state['current_page']="Sign_In"

def render():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
def about():
    user = st.session_state['signed_in_user']
    if user is None:
        st.sidebar.header("")
    else:
        st.sidebar.header(st.session_state['signed_in_user']['Name'])
    st.header("About Us")
    with open('about.txt', 'r') as file:
        content =file.read()
    st.write(content)
    st.link_button("Read more", url="https://en.wikipedia.org/wiki/Swiggy")

about()