import streamlit as st
st.set_page_config(
    page_title="Swiggy",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image("img.png", caption="Swiggy")
import pandas as pd

#reading the menu database
df=pd.read_csv("database/menu.csv", sep=',')

#reading the signed in users database
df1=pd.read_csv("database/user_data.csv")

if "cart" not in st.session_state:
    st.session_state["cart"] = []

if "signed_in_user" not in st.session_state:
    st.session_state["signed_in_user"] = None

def cart():
    st.sidebar.header("Your Cart")
    if st.session_state["cart"]:
        total_price = 0
        for item in st.session_state["cart"]:
            st.sidebar.write(f"- {item['Food Item']} (₹{item['Price (INR)']})")
            total_price += item["Price (INR)"]
        st.sidebar.write(f"**Total: ₹{total_price}**")

        if st.sidebar.button("Clear Cart"):
            st.session_state["cart"] = []
            st.sidebar.success("Cart cleared!")
            st.rerun()
    else:
        st.sidebar.write("Your cart is empty.")

# Add to Cart Logic
def add_to_cart(food_item):
    for index, row in df.iterrows():
        if row["Food Item"] == food_item:
            st.session_state["cart"].append(row)
            st.success(f"{food_item} added to cart!")
            break

def home():
    user=st.session_state['signed_in_user']
    if user is None:
        st.sidebar.header("Not signed in")
        st.error("Please sign in first to access the App!")
    else:
        st.sidebar.header(st.session_state['signed_in_user']['Name'])
        if st.sidebar.button("Log out"):
            st.session_state["signed_in_user"] = None
            st.rerun()
        col1, col2 = st.columns([10,1])  # Adjust column width proportions as needed
        with col1:
            search_bar = st.text_input("Enter the food to be searched", placeholder="Search", label_visibility="collapsed",
                                       key="search_bar")
        with col2:
            search_button = st.button("Search")
        choose = st.selectbox("Select a category to see the Menu", ['','Veg', 'Non-Veg','All'],placeholder="Category")#inserting filter box
        price=st.slider("Price",min_value=0,max_value=600,value=0,step=1)
        found=False
        if search_button and search_bar == '':#if no item is inserted inside the search bar and search has started
            st.error("Pls enter the item first")
        else:
            for index,row in df.iterrows():
                if search_button and search_bar in row['Food Item']:
                    found=True#checking whether the searched item is there in the menu
                    st.write(f'<p style="font-size:20px;font-family:Times;">{row['Food Item']}</p>',
                             unsafe_allow_html=True)#displaying the name of the food
                    st.image(f"images/{row['Path']}", width=300)#displaying the image of the food
                    break
            if search_button and not found:
                st.error("Item not found")
            col4,_,col5=st.columns([3,1,3])
            if choose=='All':
                if price:
                    with col4:
                        for index,row in df[:5].iterrows():
                            if row['Price (INR)']<=price:
                                st.write(f'<p style="font-size:15px;font-family:Times;">{row['Food Item']}</p>',
                                         unsafe_allow_html=True)
                                st.image(f"images/{row['Path']}",width=300)
                                col9,col10=st.columns([5,7])
                                with col9:
                                    st.write(f'<p style="font-size:15px;font-family:Times;">₹{row['Price (INR)']}</p>',
                                         unsafe_allow_html=True)
                                with col10:
                                    if st.button(f"Add to Cart", key=f"cart_{row['Food Item']}"):
                                        add_to_cart(row["Food Item"])

                    with col5:
                        for index,row in df[5:10].iterrows():
                            if row['Price (INR)']<=price:
                                st.write(f'<p style="font-size:15px;font-family:Times;">{row['Food Item']}</p>',
                                         unsafe_allow_html=True)
                                st.image(f"images/{row['Path']}",width=300)
                                col11,col12=st.columns([5,7])
                                with col11:
                                    st.write(f'<p style="font-size:15px;font-family:Times;">₹{row['Price (INR)']}</p>',
                                         unsafe_allow_html=True)
                                with col12:
                                    if st.button(f"Add to Cart", key=f"cart_{row['Food Item']}"):
                                        add_to_cart(row["Food Item"])
                else:
                    with col4:
                        for index, row in df[:5].iterrows():
                            st.write(f'<p style="font-size:15px;font-family:Times;">{row['Food Item']}</p>',
                                     unsafe_allow_html=True)
                            st.image(f"images/{row['Path']}", width=300)
                            col9, col10 = st.columns([5, 7])
                            with col9:
                                st.write(
                                    f'<p style="font-size:15px;font-family:Times;">₹{row['Price (INR)']}</p>',
                                    unsafe_allow_html=True)
                            with col10:
                                if st.button(f"Add to Cart", key=f"cart_{row['Food Item']}"):
                                    add_to_cart(row["Food Item"])

                    with col5:
                        for index, row in df[5:10].iterrows():
                            st.write(f'<p style="font-size:15px;font-family:Times;">{row['Food Item']}</p>',
                                     unsafe_allow_html=True)
                            st.image(f"images/{row['Path']}", width=300)
                            col11, col12 = st.columns([5, 7])
                            with col11:
                                st.write(
                                    f'<p style="font-size:15px;font-family:Times;">₹{row['Price (INR)']}</p>',
                                    unsafe_allow_html=True)
                            with col12:
                                if st.button(f"Add to Cart", key=f"cart_{row['Food Item']}"):
                                    add_to_cart(row["Food Item"])

            elif choose!='':
                st.write(f'<p style="font-size:15px;font-family:Times;">Results for:{choose}</p>',unsafe_allow_html=True)
                if price:
                    for index,row in df.iterrows():
                        if row['Key'] == choose and row['Price (INR)']<=price:
                            st.write(f'<p style="font-size:20px;font-family:Times;">{row['Food Item']}</p>',
                                     unsafe_allow_html=True)
                            st.image(f"images/{row['Path']}", width=300)
                            col11,col12=st.columns([5,25])
                            with col11:
                                st.write(f'<p style="font-size:15px;font-family:Times;">₹{row['Price (INR)']}</p>',
                                     unsafe_allow_html=True)
                            with col12:
                                if st.button(f"Add to Cart", key=f"cart_{row['Food Item']}"):
                                    add_to_cart(row["Food Item"])
                elif not price:
                    for index,row in df.iterrows():
                        if row['Key'] == choose:
                            st.write(f'<p style="font-size:20px;font-family:Times;">{row['Food Item']}</p>',
                                     unsafe_allow_html=True)
                            st.image(f"images/{row['Path']}", width=300)
                            col11,col12=st.columns([5,25])
                            with col11:
                                st.write(f'<p style="font-size:15px;font-family:Times;">₹{row['Price (INR)']}</p>',
                                     unsafe_allow_html=True)
                            with col12:
                                if st.button(f"Add to Cart", key=f"cart_{row['Food Item']}"):
                                    add_to_cart(row["Food Item"])
        cart()
home()




