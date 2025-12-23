import streamlit as st
import time

st.set_page_config(page_title="Pizza Chatbot 🍕")

st.title("🍕 Pizza Order Chatbot")

menu = {
    "Margherita": 500,
    "Pepperoni": 700,
    "BBQ Chicken": 800
}

if "order" not in st.session_state:
    st.session_state.order = []

st.write("### Menu")
for item, price in menu.items():
    st.write(f"{item} - Rs {price}")

choice = st.selectbox("Pizza choose karo:", list(menu.keys()))

if st.button("Order Add karo"):
    st.session_state.order.append(choice)
    st.success(f"{choice} order mein add ho gaya")

if st.session_state.order:
    st.write("### Tumhara Order:")
    total = 0
    for item in st.session_state.order:
        st.write(item)
        total += menu[item]

    st.write(f"### Total Bill: Rs {total}")

    if st.button("Place Order"):
        st.info("Order place ho raha hai...")
        time.sleep(2)
        st.success("🍕 Order Confirmed!")
        st.info("⏱️ 30 minutes mein deliver ho jayega")
