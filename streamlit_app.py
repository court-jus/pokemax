import streamlit as st
import random
from pokedex import POKEDEX

def afficher_liste():
    for pokemon in POKEDEX:
        st.write(pokemon.decris_toi())

def afficher_un_au_hasard():
    pokemon = random.choice (POKEDEX)
    st.write(pokemon.decris_toi())


def page_principale():
    st.title("👾 Mon pokédex")
    st.write("Mon premier pokédex")
    afficher_liste()

page_principale()
