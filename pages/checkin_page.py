import streamlit as st
import sqlite3
from datetime import datetime

st.title("Visitor Check-in")

# Connect to SQLite database
conn = sqlite3.connect("checkin_system.db")
cursor = conn.cursor()

# Create visitors table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        purpose TEXT,
        checkin_time TEXT,
        status TEXT DEFAULT 'Pending'
    )
""")
conn.commit()

# Check-in form
with st.form("checkin_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    purpose = st.text_area("Purpose of Visit")
    submit = st.form_submit_button("Check-in")

if submit:
    checkin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO visitors (name, email, purpose, checkin_time, status) VALUES (?, ?, ?, ?, ?)", 
                   (name, email, purpose, checkin_time, "Pending"))
    conn.commit()

    # Save email in session state for status checking
    st.session_state["last_checked_email"] = email  

    st.success("✅ Check-in Successful! Please wait for admin approval.")

    # Provide a link to check status
    st.markdown(f"[Check Status](status)")
conn.close()
