import streamlit as st
import sqlite3

def admin_dashboard():
    if not st.session_state.admin_logged_in:
        st.warning("Please log in to access the admin dashboard.")
        return

    st.title("Admin Dashboard")

    conn = sqlite3.connect("checkin_system.db")
    cursor = conn.cursor()

    # Fetch pending visitors
    cursor.execute("SELECT * FROM visitors WHERE status = 'Pending'")
    visitors = cursor.fetchall()

    if not visitors:
        st.write("No pending visitors.")
    else:
        for visitor in visitors:
            st.subheader(f"Visitor: {visitor[1]}")
            st.write(f"Email: {visitor[2]}")
            st.write(f"Purpose: {visitor[3]}")
            st.write(f"Check-in Time: {visitor[4]}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Accept {visitor[1]}", key=f"accept_{visitor[0]}"):
                    cursor.execute("UPDATE visitors SET status='Accepted' WHERE id=?", (visitor[0],))
                    conn.commit()
                    st.success(f"{visitor[1]} Accepted")

            with col2:
                if st.button(f"Reject {visitor[1]}", key=f"reject_{visitor[0]}"):
                    cursor.execute("UPDATE visitors SET status='Rejected' WHERE id=?", (visitor[0],))
                    conn.commit()
                    st.error(f"{visitor[1]} Rejected")

    # Visitor History
    st.subheader("Visitor History")
    cursor.execute("SELECT * FROM visitors WHERE status != 'Pending'")
    history = cursor.fetchall()

    for visitor in history:
        st.write(f"**{visitor[1]}** - {visitor[5]}")

    conn.close()

    # Logout Button
    if st.button("Logout"):
        st.session_state.admin_logged_in = False
        st.experimental_rerun()
