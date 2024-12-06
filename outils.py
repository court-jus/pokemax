import streamlit as st

def affiche_liste(textes):
    st.markdown("\n".join(f"* {texte}" for texte in textes))
