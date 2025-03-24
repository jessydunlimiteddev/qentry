import streamlit as st
import sqlite3
from pages.signup import hash_password

# Admin Login Page
def admin_login():
    st.title("Admin Login")

    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    conn = sqlite3.connect("checkin_system.db")
    cursor = conn.cursor()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        hashed_password = hash_password(password)
        cursor.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, hashed_password))
        admin = cursor.fetchone()

        if admin:
            st.session_state.admin_logged_in = True
            st.session_state.admin_username = username  # Store username in session
            st.success("Login Successful!")
            
        else:
            st.error("Invalid credentials")

    conn.close()
