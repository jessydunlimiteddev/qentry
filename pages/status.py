import streamlit as st
import sqlite3

st.title("Check-in Status")

# Connect to SQLite database
conn = sqlite3.connect("checkin_system.db")
cursor = conn.cursor()

# Pre-fill email if available in session state
email = st.text_input("Enter your email to check your check-in status:", 
                      value=st.session_state.get("last_checked_email", ""))

if st.button("Check Status"):
    cursor.execute("SELECT status FROM visitors WHERE email = ? ORDER BY checkin_time DESC LIMIT 1", (email,))
    result = cursor.fetchone()
    
    if result:
        status = result[0]
        if status == "Accepted":
            st.success("✅ Your check-in has been approved! You may proceed.")
        elif status == "Rejected":
            st.error("❌ Your check-in request was rejected.")
        else:
            st.warning("⏳ Your check-in is still pending approval. Please wait.")
    else:
        st.error("⚠️ No check-in record found for this email. Please check if you entered the correct email.")

conn.close()
