import streamlit as st

st.set_page_config(
    page_title="Your App Name",
    initial_sidebar_state="expanded",
    layout="wide"  # optional
)

# Titulek aplikace
st.title("Moje Streamlit Aplikace na AWS App Runner")

# Jednoduchý vstup a výstup
name = st.text_input("Zadej své jméno:")
if name:
    st.write(f"Ahoj, {name}! 👋")

# Tlačítko pro zobrazení zprávy
if st.button("Klikni mě!"):
    st.success("Gratulujeme, aplikace běží na AWS App Runner! 🚀")

# Footer
st.write("Tato aplikace běží na **Streamlit** a je hostována na **AWS App Runner**.")

