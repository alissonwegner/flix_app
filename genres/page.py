import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comedia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
   
]
def show_genres():
    st.write('Lista de Generos:')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',   
           )
    st.title('Cadastrar novo Genero')
    name = st.text_input('Nome do Genero')
    if st.button('Cadastrar'):
        st.success(f'Genero {name} cadastrado com sucesso!')