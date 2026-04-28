# streamlit_app.py
# A simple Streamlit QR Code Generator for links, numbers, and text/info

import streamlit as st
import qrcode
from io import BytesIO

# Page config
st.set_page_config(page_title="QR Code Generator", page_icon="🔳", layout="centered")

st.title("🔳 QR Code Generator")
st.write("Convert a link, phone number, or any text/info into a QR code instantly.")

# Input type selection
qr_type = st.selectbox(
    "Choose what you want to convert:",
    ["Website Link", "Phone Number", "Text / Info"]
)

# User input
user_input = ""

if qr_type == "Website Link":
    user_input = st.text_input("Enter website URL:", placeholder="https://example.com")

elif qr_type == "Phone Number":
    phone = st.text_input("Enter phone number:", placeholder="+1234567890")
    if phone:
        user_input = f"tel:{phone}"

elif qr_type == "Text / Info":
    user_input = st.text_area("Enter your text or information:")

# QR generation settings
fill_color = st.color_picker("QR Color", "#000000")
back_color = st.color_picker("Background Color", "#FFFFFF")

# Generate QR Code
if st.button("Generate QR Code"):
    if user_input.strip():
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        qr.add_data(user_input)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Save image to buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Display image
        st.image(buffer, caption="Your QR Code", use_column_width=False)

        # Download button
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )

    else:
        st.warning("Please enter valid input before generating the QR code.")

# Footer
st.markdown("---")
st.caption("Built with Streamlit + qrcode")