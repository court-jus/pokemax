import streamlit as st
import random
from pokedex import POKEDEX
from outils import affiche_liste

def afficher_tous_les_pokemons():
    descriptions = []
    for pokemon in POKEDEX:
        descriptions.append(pokemon.decris_toi())
        
    affiche_liste(descriptions)

def afficher_un_au_hasard():
    pokemon = random.choice (POKEDEX)
    st.write(pokemon.decris_toi())


def page_principale():
    st.title("👾 Mon pokédex")
    st.write("Mon premier pokédex")
    afficher_tous_les_pokemons()

page_principale()
