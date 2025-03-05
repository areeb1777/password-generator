import streamlit as st
import random
import string
import math


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def evaluate_password_strength(password):
    length_score = min(len(password) / 32, 1.0)
    digit_score = 0.2 if any(char.isdigit() for char in password) else 0
    special_score = 0.3 if any(char in string.punctuation for char in password) else 0
    upper_lower_score = 0.5 if any(char.islower() for char in password) and any(char.isupper() for char in password) else 0

    total_score = length_score + digit_score + special_score + upper_lower_score

    normalized_score = min(total_score, 1.0)

    if total_score < 0.5:
        return "Weak", normalized_score
    elif total_score < 0.8:
        return "Medium", normalized_score
    else:
        return "Strong", normalized_score

st.title("🔒 Password Generator & Strength Checker")

st.sidebar.header("⚙️ Customize Your Password")
length = st.sidebar.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.sidebar.checkbox("Include Digits", value=True)
use_special = st.sidebar.checkbox("Include Special Characters", value=True)

st.markdown("## 📝 Check Your Password Strength")
manual_password = st.text_input("Enter your password to check its strength:")
if st.button("Check Strength"):
    if manual_password:
        strength, score = evaluate_password_strength(manual_password)
        st.markdown(
            f"### Manual Password Strength: **{strength}** ({math.ceil(score * 100)}%)"
        )
        st.progress(score)
    else:
        st.warning("Please enter a password to check its strength!")

st.markdown("---")
st.markdown("## 🔑 Generate a New Password")
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

    strength, score = evaluate_password_strength(password)
    st.markdown(
        f"### Generated Password Strength: **{strength}** ({math.ceil(score * 100)}%)"
    )
    st.progress(score)

st.markdown("---")
st.markdown(
    """
    Made with ❤ by **[Areeb Malik](https://github.com/areeb1777)**  
    """
)
