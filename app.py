import streamlit as st
import base64
import hashlib

from cryptography.fernet import Fernet

# --------------------
# PAGE CONFIG
# --------------------

st.set_page_config(
    page_title="CipherVault",
    page_icon="🔒",
    layout="wide"
)

# --------------------
# CSS
# --------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #050505,
        #0d1117
    );
    color:white;
}

.big-title{
    text-align:center;
    font-size:64px;
    font-weight:800;
    color:#00ffcc;
    text-shadow:0 0 20px #00ffcc;
}

.subtitle{
    text-align:center;
    color:#cccccc;
    margin-bottom:30px;
}

.cyber-box{
    border:1px solid #00ffcc;
    border-radius:15px;
    padding:25px;
    background:rgba(255,255,255,0.03);
    box-shadow:0px 0px 25px rgba(0,255,204,0.2);
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# --------------------
# TITLE
# --------------------

st.markdown(
    '<div class="big-title">🔒 CipherVault</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Secure Message Encryption Laboratory</div>',
    unsafe_allow_html=True
)

# --------------------
# MATRIX STYLE ANIMATION
# --------------------

st.markdown("""
<marquee scrollamount="8">
01001010 10110101 01101001 11010101
01101001 01010101 11100011 00110011
10101010 11010101 00110110 11110000
</marquee>
""", unsafe_allow_html=True)

# --------------------
# KEY GENERATION
# --------------------

def password_to_key(password):

    digest = hashlib.sha256(
        password.encode()
    ).digest()

    return base64.urlsafe_b64encode(
        digest
    )

# --------------------
# MODE
# --------------------

mode = st.radio(
    "Select Mode",
    ["Encrypt","Decrypt"]
)

password = st.text_input(
    "Password",
    type="password"
)

# --------------------
# ENCRYPT
# --------------------

if mode == "Encrypt":

    msg = st.text_area(
        "Message"
    )

    if st.button("🔒 Encrypt"):

        if msg and password:

            key = password_to_key(password)

            f = Fernet(key)

            encrypted = f.encrypt(
                msg.encode()
            )

            st.success(
                "Encryption Successful"
            )

            st.code(
                encrypted.decode()
            )

            st.balloons()

# --------------------
# DECRYPT
# --------------------

else:

    cipher = st.text_area(
        "Encrypted Message"
    )

    if st.button("🔓 Decrypt"):

        try:

            key = password_to_key(password)

            f = Fernet(key)

            result = f.decrypt(
                cipher.encode()
            )

            st.success(
                "Decryption Successful"
            )

            st.code(
                result.decode()
            )

        except:

            st.error(
                "Invalid password or message."
            )

st.divider()

st.markdown(
    '<div class="footer">Built by Del Ho</div>',
    unsafe_allow_html=True
)
