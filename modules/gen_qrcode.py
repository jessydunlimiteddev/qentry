import qrcode
import qrcode
from io import BytesIO

def generate_qr():
    url = "https://qentryy.streamlit.app/checkin_page"  
    qr = qrcode.make(url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    return buf.getvalue()

