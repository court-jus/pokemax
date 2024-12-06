import streamlit as st
from outils import affiche_liste

st.title("👾 Mon pokédex")
st.write(
    "Mon premier pokédex"
)
affiche_liste(["toto", "tata"])