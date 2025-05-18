import streamlit as st
from abc import ABC, abstractmethod

# Abstract base classes
class Auth(ABC):
    @abstractmethod
    def login(self):
        pass

class SignUp(ABC):
    @abstractmethod
    def sign_up(self):
        pass

# Implementations
class LoginPassword(Auth, SignUp):
    def login(self, email, password):
        if email and password:
            return f"✅ Logged in with **{email}**"
        return "❌ Login Failed: Please enter both email and password."
    
    def sign_up(self):
        return "📧 Signed up using email and password!"

class GoogleAuth(Auth, SignUp):
    def login(self):
        return "🔗 Redirecting to **Google Auth**..."
    
    def sign_up(self):
        return "🆕 Signing up with **Google**..."

class FaceBookAuth(Auth, SignUp):
    def login(self):
        return "🔗 Redirecting to **Facebook Auth**..."
    
    def sign_up(self):
        return "🆕 Signing up with **Facebook**..."

# Streamlit UI
st.title("🔐 Multi-Auth System with Streamlit")

choose_auth = st.selectbox("👇 Choose Authentication Method", ["📧 Email/Password", "🟢 Google", "🔵 Facebook"])

if choose_auth == "📧 Email/Password":
    st.subheader("📥 Login / Sign Up with Email")
    email = st.text_input("✉️ Enter Email")
    password = st.text_input("🔑 Enter Password", type="password")

    user = LoginPassword()
    if st.button("🔓 Login"):
        st.success(user.login(email, password))
    if st.button("🆕 Sign Up"):
        st.success(user.sign_up())

elif choose_auth == "🟢 Google":
    st.subheader("🔐 Google Authentication")
    user = GoogleAuth()
    if st.button("🔓 Login with Google"):
        st.success(user.login())
    if st.button("🆕 Sign Up with Google"):
        st.success(user.sign_up())

elif choose_auth == "🔵 Facebook":
    st.subheader("🔐 Facebook Authentication")
    user = FaceBookAuth()
    if st.button("🔓 Login with Facebook"):
        st.success(user.login())
    if st.button("🆕 Sign Up with Facebook"):
        st.success(user.sign_up())
