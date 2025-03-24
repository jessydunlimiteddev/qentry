import streamlit as st
from pages.admin import admin_dashboard
from pages.login import admin_login
from pages.signup import admin_signup

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Admin Signup", 
    "Admin Login", 
    "Admin Dashboard"
])

if page == "Admin Signup":
    admin_signup()
elif page == "Admin Login":
    admin_login()
elif page == "Admin Dashboard":
    admin_dashboard()
