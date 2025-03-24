import streamlit as st
from pages.admin import admin_dashboard
from pages.login import admin_login
from pages.signup import admin_signup

# Initialize session state for page navigation if it doesn't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Function to update page in session state
def set_page(page_name):
    st.session_state.current_page = page_name

# Custom CSS for a better landing page
def load_css():
    st.markdown("""
    <style>
        /* Main container styling */
        .main .block-container {
            padding-top: 1rem;
            max-width: 1200px;
        }
        
        /* Header styling */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            border-bottom: 1px solid #E5E7EB;
            margin-bottom: 2rem;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #1E3A8A;
        }
        
        /* Hero section */
        .hero {
            text-align: center;
            padding: 3rem 1rem;
            background-color: #F9FAFB;
            border-radius: 12px;
            margin-bottom: 2rem;
        }
        
        .hero h1 {
            color: #1E3A8A;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            color: #4B5563;
            font-size: 1.25rem;
            max-width: 800px;
            margin: 0 auto 2rem auto;
        }
        
        /* Card styling */
        .card {
            background-color: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            text-align: center;
            height: 100%;
        }
        
        .card-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #2563EB;
        }
        
        .card h3 {
            color: #1F2937;
            margin-bottom: 0.5rem;
        }
        
        .card p {
            color: #6B7280;
            margin-bottom: 1rem;
        }
        
        /* Footer */
        .footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #E5E7EB;
            text-align: center;
            color: #6B7280;
        }
        
        /* Button styling */
        .stButton > button {
            border-radius: 6px;
            font-weight: 500;
            padding: 0.5rem 1.5rem;
            background-color: #2563EB;
            color: white;
            width: 100%;
        }
        
        .stButton > button:hover {
            background-color: #1D4ED8;
        }
        
        /* Active button styling */
        .active-button > button {
            background-color: #1E40AF;
            border: 2px solid #3B82F6;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Home page / Landing page
def home():
    st.markdown("""
    <div class="hero">
        <h1>Visitor Management System</h1>
        <p>A streamlined solution for managing visitor check-ins, approvals, and tracking at your facility.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation cards with buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">👤</div>
            <h3>Admin Signup</h3>
            <p>Create a new admin account to manage visitors</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Signup", key="signup_btn"):
            set_page("Admin Signup")
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🔑</div>
            <h3>Admin Login</h3>
            <p>Access your dashboard to approve or reject visitors</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Login", key="login_btn"):
            set_page("Admin Login")
    
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">📊</div>
            <h3>Admin Dashboard</h3>
            <p>View and manage all visitor requests</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Dashboard", key="dashboard_btn"):
            set_page("Admin Dashboard")
    
    st.markdown("""
    <div class="footer">
        <p>© 2023 Visitor Management System. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

# Main app
def main():
    # Load custom CSS
    load_css()
    
    # Create header with logo
    st.markdown("""
    <div class="header">
        <div class="logo">Visitor Management System</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons in a row
    col1, col2, col3, col4 = st.columns(4)
    
    # Apply different styling to the active button using custom CSS classes
    with col1:
        button_class = "active-button" if st.session_state.current_page == "Home" else ""
        st.markdown(f'<div class="{button_class}">', unsafe_allow_html=True)
        if st.button("Home", key="home_nav"):
            set_page("Home")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        button_class = "active-button" if st.session_state.current_page == "Admin Signup" else ""
        st.markdown(f'<div class="{button_class}">', unsafe_allow_html=True)
        if st.button("Signup", key="signup_nav"):
            set_page("Admin Signup")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        button_class = "active-button" if st.session_state.current_page == "Admin Login" else ""
        st.markdown(f'<div class="{button_class}">', unsafe_allow_html=True)
        if st.button("Login", key="login_nav"):
            set_page("Admin Login")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        button_class = "active-button" if st.session_state.current_page == "Admin Dashboard" else ""
        st.markdown(f'<div class="{button_class}">', unsafe_allow_html=True)
        if st.button("Dashboard", key="dashboard_nav"):
            set_page("Admin Dashboard")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Display the current page based on session state
    if st.session_state.current_page == "Home":
        home()
    elif st.session_state.current_page == "Admin Signup":
        admin_signup()
    elif st.session_state.current_page == "Admin Login":
        admin_login()
    elif st.session_state.current_page == "Admin Dashboard":
        admin_dashboard()

if __name__ == "__main__":
    main()

