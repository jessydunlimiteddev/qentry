import streamlit as st
from modules.gen_qrcode import generate_qr

st.title("Scan to Check-in")

# Display the QR code
st.image(generate_qr(), caption="Scan this QR Code to Check-in", use_container_width=True)

st.write("Once you scan the QR code, you will be directed to the check-in form.")
