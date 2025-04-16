import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        strength = "✅ **Strong Password!**"
    elif score == 3:
        strength = "⚠️ **Moderate Password**"
    else:
        strength = "❌ **Weak Password**"

    return strength, feedback


st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength:")

password = st.text_input("🔑 Enter Password", type="password")

if st.button("Check Strength"):
    if password:
        strength, feedback = check_password_strength(password)
        st.markdown(strength)
        if feedback:
            st.subheader("Suggestions:")
            for f in feedback:
                st.write("- " + f)
    else:
        st.warning("Please enter a password first.")

