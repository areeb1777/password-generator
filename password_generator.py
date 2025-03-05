import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔒 Password Generator")

st.markdown(
    """
    Welcome to the **Password Generator**! 🎉
    Secure your accounts with strong, custom passwords. 
    Adjust the settings below and click 'Generate Password' to get started.
    """
)

st.sidebar.header("⚙️ Customize Your Password")
length = st.sidebar.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.sidebar.checkbox("Include Digits", value=True)
use_special = st.sidebar.checkbox("Include Special Characters", value=True)

if st.button("Generate Password 🔑"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Your Generated Password: `{password}`")

st.markdown("---")
st.markdown(
    """
    Made with ❤ by **[Areeb Malik](https://github.com/areeb1777)**  
    """
)
