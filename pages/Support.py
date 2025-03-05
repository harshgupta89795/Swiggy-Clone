import streamlit as st
from sendmail import send_email

def contact_us():
    user = st.session_state['signed_in_user']
    if user is None:
        st.sidebar.header("")
    else:
        st.sidebar.header(st.session_state['signed_in_user']['Name'])
    st.subheader("You can contact us 24*7")
    with st.form(key="support"):
        user_email=st.text_input("Enter you Email Address")
        user_query=st.text_area("Enter your Query")
        raw_message = f"""\
        Subject: Query from {user_email}
        Message:
        {user_query}
        """
        but=st.form_submit_button("Submit")
        if but:
            send_email(user_query)
            st.info("Your Query has been taken into Consideration")

contact_us()