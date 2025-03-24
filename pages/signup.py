import hashlib
import streamlit as st
import sqlite3

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Admin Signup Page
def admin_signup():
    st.title("Admin Signup")

    conn = sqlite3.connect("checkin_system.db")
    cursor = conn.cursor()

    with st.form("signup_form"):
        username = st.text_input("Choose a Username")
        password = st.text_input("Choose a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Sign Up")

    if submit:
        if password != confirm_password:
            st.error("Passwords do not match!")
        else:
            hashed_password = hash_password(password)
            try:
                cursor.execute("INSERT INTO admins (username, password) VALUES (?, ?)", (username, hashed_password))
                conn.commit()
                st.success("Admin account created successfully! Please log in.")
            except sqlite3.IntegrityError:
                st.error("Username already exists. Choose a different one.")

    conn.close()
