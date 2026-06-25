import streamlit as st
import hashlib
import base64
import time
from cryptography.fernet import Fernet

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="CipherVault",
    page_icon="🔒",
    layout="centered"
)

# -----------------------------
# STYLING
# -----------------------------

st.markdown("""
<style>

.stApp {
    background-color: #0d1117;
}

.main-title {
    text-align: center;
    color: #00ffcc;
    font-size: 3rem;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #aaaaaa;
    margin-bottom: 25px;
}

.cyber-box {
    border: 1px solid #00ffcc;
    padding: 20px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="main-title">🔒 CipherVault</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Secure Message Encryption Laboratory</div>',
    unsafe_allow_html=True
)

st.code(
    "01001010 10110101 01101001 11010101 11100011 00110011",
    language=None
)

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def password_to_key(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)




# -----------------------------
# USER INPUT
# -----------------------------

mode = st.radio(
    "Mode",
    ["Encrypt", "Decrypt"]
)

password = st.text_input(
    "Password",
    type="password"
)

# -----------------------------
# ENCRYPT MODE
# -----------------------------

if mode == "Encrypt":

    message = st.text_area(
        "Message to Encrypt"
    )

    if st.button("🔒 Encrypt"):

        if not password or not message:
            st.warning(
                "Please enter a password and message."
            )

        else:

            

            status = st.empty()

            progress = st.progress(0)

            steps = [
                "Generating SHA-256 hash...",
                "Deriving encryption key...",
                "Encrypting message...",
                "Securing vault...",
                "Finalizing..."
            ]

            for i in range(5):

                status.info(steps[i])

                for p in range(20):
                    progress.progress(i * 20 + p + 1)
                    time.sleep(0.05)

            key = password_to_key(password)

            f = Fernet(key)

            encrypted = f.encrypt(
                message.encode()
            )

            st.success(
                "Encryption Complete"
            )

            st.code(
                encrypted.decode(),
                language=None
            )

            st.balloons()

# -----------------------------
# DECRYPT MODE
# -----------------------------

else:

    encrypted_message = st.text_area(
        "Encrypted Message"
    )

    if st.button("🔓 Decrypt"):

        if not password or not encrypted_message:
            st.warning(
                "Please enter a password and encrypted message."
            )

        else:

            

            status = st.empty()

            progress = st.progress(0)

            steps = [
                "Validating password...",
                "Generating SHA-256 hash...",
                "Rebuilding key...",
                "Decrypting vault...",
                "Unlocking..."
            ]

            for i in range(5):

                status.info(steps[i])

                for p in range(20):
                    progress.progress(i * 20 + p + 1)
                    time.sleep(0.05)

            try:

                key = password_to_key(password)

                f = Fernet(key)

                decrypted = f.decrypt(
                    encrypted_message.encode()
                )

                st.success(
                    "Decryption Complete"
                )

                st.code(
                    decrypted.decode(),
                    language=None
                )

            except:

                st.error(
                    "Invalid password or encrypted message."
                )

st.divider()

st.caption(
    "Built by Del Ho | Python • Streamlit • Cryptography"
)
