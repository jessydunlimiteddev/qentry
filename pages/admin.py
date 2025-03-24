import streamlit as st
import sqlite3

# Custom CSS to improve the visual appearance
def load_css():
    st.markdown("""
    <style>
        /* Main container styling */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Header styling */
        h1 {
            color: #1E3A8A;
            padding-bottom: 1rem;
            border-bottom: 2px solid #E5E7EB;
        }
        
        h2 {
            color: #1E3A8A;
            margin-top: 1.5rem;
        }
        
        h3 {
            color: #1F2937;
            margin-top: 1rem;
        }
        
        /* Visitor card styling */
        .visitor-card {
            background-color: #F9FAFB;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 4px solid #3B82F6;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .visitor-info {
            margin-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            font-weight: 500;
        }
        
        .accept-btn > button {
            background-color: #10B981;
            color: white;
        }
        
        .accept-btn > button:hover {
            background-color: #059669;
        }
        
        .reject-btn > button {
            background-color: #EF4444;
            color: white;
        }
        
        .reject-btn > button:hover {
            background-color: #DC2626;
        }
        
        .logout-btn > button {
            background-color: #6B7280;
            color: white;
        }
        
        .logout-btn > button:hover {
            background-color: #4B5563;
        }
        
        /* History section styling */
        .history-section {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #E5E7EB;
        }
        
        .history-item {
            padding: 0.75rem;
            border-radius: 6px;
            margin-bottom: 0.5rem;
        }
        
        .status-accepted {
            background-color: #D1FAE5;
            border-left: 3px solid #10B981;
        }
        
        .status-rejected {
            background-color: #FEE2E2;
            border-left: 3px solid #EF4444;
        }
    </style>
    """, unsafe_allow_html=True)

def admin_dashboard():
    # Load custom CSS
    load_css()
    
    if not st.session_state.admin_logged_in:
        st.warning("Please log in to access the admin dashboard.")
        return

    st.title("Admin Dashboard")

    conn = sqlite3.connect("checkin_system.db")
    cursor = conn.cursor()

    # Fetch pending visitors
    cursor.execute("SELECT * FROM visitors WHERE status = 'Pending'")
    visitors = cursor.fetchall()

    st.subheader("Pending Visitors")
    
    if not visitors:
        st.info("No pending visitors.")
    else:
        for visitor in visitors:
            # Create a styled visitor card
            st.markdown(f"""
            <div class="visitor-card">
                <h3>{visitor[1]}</h3>
                <div class="visitor-info">📧 <b>Email:</b> {visitor[2]}</div>
                <div class="visitor-info">🎯 <b>Purpose:</b> {visitor[3]}</div>
                <div class="visitor-info">⏰ <b>Check-in Time:</b> {visitor[4]}</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                # Add custom class for styling
                st.markdown('<div class="accept-btn">', unsafe_allow_html=True)
                if st.button(f"Accept {visitor[1]}", key=f"accept_{visitor[0]}"):
                    cursor.execute("UPDATE visitors SET status='Accepted' WHERE id=?", (visitor[0],))
                    conn.commit()
                    st.success(f"{visitor[1]} Accepted")
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                # Add custom class for styling
                st.markdown('<div class="reject-btn">', unsafe_allow_html=True)
                if st.button(f"Reject {visitor[1]}", key=f"reject_{visitor[0]}"):
                    cursor.execute("UPDATE visitors SET status='Rejected' WHERE id=?", (visitor[0],))
                    conn.commit()
                    st.error(f"{visitor[1]} Rejected")
                st.markdown('</div>', unsafe_allow_html=True)

    # Visitor History
    st.markdown('<div class="history-section">', unsafe_allow_html=True)
    st.subheader("Visitor History")
    cursor.execute("SELECT * FROM visitors WHERE status != 'Pending'")
    history = cursor.fetchall()

    if not history:
        st.info("No visitor history yet.")
    else:
        for visitor in history:
            status_class = "status-accepted" if visitor[5] == "Accepted" else "status-rejected"
            st.markdown(f"""
            <div class="history-item {status_class}">
                <b>{visitor[1]}</b> - {visitor[5]} | <small>{visitor[4]}</small>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    conn.close()

    # Logout Button
    st.markdown('<div class="logout-btn" style="margin-top: 2rem;">', unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.admin_logged_in = False
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

