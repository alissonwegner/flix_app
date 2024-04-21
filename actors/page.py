import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

actors = [
    {
        'id': 1,
        'name': 'Leonardo'
    },
    {
        'id': 2,
        'name': 'Chris Rock'
    },
    {
        'id': 3,
        'name': 'Stallone'
    },
   
]
def show_actores():
    st.write('Lista de Atores:')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',   
           )
    st.title('Cadastrar novo Ator')
    name = st.text_input('Nome do Ator')
    if st.button('Cadastrar'):
        st.success(f'Ator {name} cadastrado com sucesso!')