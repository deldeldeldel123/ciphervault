import streamlit as st
import base64
import hashlib
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

# STYLING

# =====================================

st.markdown("""

<style>

.stApp{
    background: linear-gradient(
        135deg,
        #050505,
        #0d1117
    );
}

.title{
    text-align:center;
    font-size:64px;
    font-weight:800;
    color:#00ffcc;
    text-shadow:0px 0px 20px #00ffcc;
}

.subtitle{
    text-align:center;
    color:#cccccc;
    margin-bottom:25px;
}

.cyber-box{
    border:1px solid #00ffcc;
    border-radius:15px;
    padding:25px;
    background:rgba(255,255,255,0.03);
    box-shadow:0px 0px 25px rgba(0,255,204,0.25);
}

.footer{
    text-align:center;
    color:gray;
}

.status-box{
    padding:15px;
    border-radius:10px;
    background:#111827;
    border:1px solid #00ffcc;
    margin-top:10px;
}

</style>

""", unsafe_allow_html=True)

# =====================================

# HEADER

# =====================================

st.markdown(
'<div class="title">🔒 CipherVault</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Secure Message Encryption Laboratory</div>',
unsafe_allow_html=True
)

# =====================================

# CYBER ANIMATION

# =====================================

st.markdown(""" <marquee scrollamount="10">
01001010 10110101 01101001 11010101
01101001 01010101 11100011 00110011
10101010 11010101 00110110 11110000
11100011 10101010 01100110 00110110 </marquee>
""", unsafe_allow_html=True)

st.divider()

# =====================================

# PASSWORD TO KEY

# =====================================

def password_to_key(password):

```
digest = hashlib.sha256(
    password.encode()
).digest()

return base64.urlsafe_b64encode(
    digest
)
```

# =====================================

# PLAY SOUND

# =====================================

def autoplay_audio(filename):

```
with open(filename, "rb") as f:
    data = f.read()

b64 = base64.b64encode(data).decode()

md = f"""
<audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
</audio>
"""

st.markdown(md, unsafe_allow_html=True)
```

# =====================================

# MODE

# =====================================

mode = st.radio(
"Select Mode",
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

```
message = st.text_area(
    "Message"
)

if st.button("🔒 Encrypt Message"):

    if not password or not message:
        st.warning(
            "Please enter a password and message."
        )

    else:

        key = password_to_key(password)

        f = Fernet(key)

        encrypted = f.encrypt(
            message.encode()
        )

        autoplay_audio("lock.mp3")

        status = st.empty()

        status.markdown(
            """
            <div class="status-box">
            🔒 Initializing encryption...
            </div>
            """,
            unsafe_allow_html=True
        )

        progress = st.progress(0)

        steps = [
            "Generating SHA-256 hash...",
            "Deriving encryption key...",
            "Securing message...",
            "Verifying integrity...",
            "Locking vault..."
        ]

        for i in range(5):

            status.markdown(
                f"""
                <div class="status-box">
                {steps[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

            for p in range(20):
                progress.progress(i * 20 + p + 1)
                time.sleep(0.05)

        st.success(
            "Encryption Successful"
        )

        st.code(
            encrypted.decode(),
            language=None
        )

        st.balloons()
```

# =====================================

# DECRYPT

# =====================================

else:

```
encrypted_text = st.text_area(
    "Encrypted Message"
)

if st.button("🔓 Decrypt Message"):

    if not password or not encrypted_text:
        st.warning(
            "Please enter a password and encrypted message."
        )

    else:

        autoplay_audio("unlock.mp3")

        status = st.empty()

        status.markdown(
            """
            <div class="status-box">
            🔓 Initializing decryption...
            </div>
            """,
            unsafe_allow_html=True
        )

        progress = st.progress(0)

        steps = [
            "Validating credentials...",
            "Generating SHA-256 hash...",
            "Rebuilding encryption key...",
            "Decrypting message...",
            "Unlocking vault..."
        ]

        for i in range(5):

            status.markdown(
                f"""
                <div class="status-box">
                {steps[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

            for p in range(20):
                progress.progress(i * 20 + p + 1)
                time.sleep(0.05)

        try:

            key = password_to_key(password)

            f = Fernet(key)

            decrypted = f.decrypt(
                encrypted_text.encode()
            )

            st.success(
                "Decryption Successful"
            )

            st.code(
                decrypted.decode(),
                language=None
            )

        except:

            st.error(
                "Invalid password or encrypted message."
            )
```

st.divider()

st.markdown(
'<div class="footer">Built by Del Ho | Python + Cryptography + Streamlit</div>',
unsafe_allow_html=True
)
