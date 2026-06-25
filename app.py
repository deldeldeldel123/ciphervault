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
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Background */
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
        0 0 20px #00ffcc;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #c0c0c0;
    margin-bottom: 20px;
}

/* Banner */
.digital-banner {
    text-align: center;
    color: #00ffcc;
    font-family: monospace;
    margin-bottom: 20px;
}

/* Buttons */
.stButton button {
    background-color: #00ffcc !important;
    color: black !important;
    font-weight: bold;
    border-radius: 8px;
    border: none;
}

/* Inputs */
.stTextInput input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #00ffcc !important;
}

.stTextArea textarea {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #00ffcc !important;
}

/* Disabled text areas (results) */
textarea[disabled] {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #00ffcc !important;
}

/* Eye icon */
[data-testid="stTextInput"] button {
    background-color: transparent !important;
    border: none !important;
}

[data-testid="stTextInput"] button svg {
    fill: #00ffcc !important;
    color: #00ffcc !important;
}

/* Code block */
pre {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #00ffcc !important;
    border-radius: 8px !important;
}

code {
    color: #ffffff !important;
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
# ENCRYPT MODE
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
# DECRYPT MODE
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

                st.text_area(
                    "Plaintext",
                    value=decrypted.decode(),
                    height=180,
                    disabled=True
                )

            except:

                st.error(
                    "Invalid password or encrypted message."
                )

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Built by Del Ho | Python • Cryptography • Streamlit"
)
