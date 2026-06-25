import streamlit as st
import hashlib
import base64
import time
from cryptography.fernet import Fernet

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="CipherVault",
    page_icon="🔒",
    layout="wide"
)

# =====================================
# CYBER CSS
# =====================================

st.markdown("""
<style>

/* Main background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #000000 0%,
        #07111f 40%,
        #001f3f 100%
    ) !important;
}

/* Hide Streamlit header */
header {
    visibility: hidden;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    color: #00ffcc;
    text-shadow:
        0 0 5px #00ffcc,
        0 0 10px #00ffcc,
        0 0 20px #00ffcc,
        0 0 40px #00ffcc;
    margin-top: 20px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #b0b0b0;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

/* Digital banner */
.digital-banner {
    color: #00ffcc;
    font-family: monospace;
    text-align: center;
    font-size: 0.9rem;
    margin-bottom: 20px;
}

/* Result box */
.result-box {
    border: 1px solid #00ffcc;
    border-radius: 10px;
    padding: 15px;
    background: rgba(0,255,204,0.05);
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    margin-top: 20px;
}

/* Buttons */
.stButton button {
    background-color: #00ffcc;
    color: black;
    font-weight: bold;
    border-radius: 8px;
    border: none;
}

/* Input fields */
/* Text input */
.stTextInput input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #00ffcc !important;
}

/* Text area */
.stTextArea textarea {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #00ffcc !important;
}

/* Placeholder text */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #888888 !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown(
    '<div class="main-title">🔒 CipherVault</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Secure Message Encryption Laboratory</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="digital-banner">
    01001010 10110101 01101001 11010101 • AES ENCRYPTION ACTIVE • SHA-256 KEY DERIVATION
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================
# FUNCTIONS
# =====================================

def password_to_key(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

# =====================================
# MODE SELECTION
# =====================================

mode = st.radio(
    "Choose Mode",
    ["Encrypt", "Decrypt"]
)

password = st.text_input(
    "Password",
    type="password"
)

# =====================================
# ENCRYPT
# =====================================

if mode == "Encrypt":

    message = st.text_area(
        "Message to Encrypt"
    )

    if st.button("🔒 Encrypt Message"):

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

            st.success("🔒 Encryption Complete")

            st.code(
                encrypted.decode(),
                language=None
            )

            st.balloons()

# =====================================
# DECRYPT
# =====================================

else:

    encrypted_message = st.text_area(
        "Encrypted Message"
    )

    if st.button("🔓 Decrypt Message"):

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

                st.success("🔓 Decryption Complete")

                st.code(
                    decrypted.decode(),
                    language=None
                )

            except:

                st.error(
                    "Invalid password or encrypted message."
                )



st.caption(
    "Built by Del Ho | Python • Cryptography • Streamlit"
)
