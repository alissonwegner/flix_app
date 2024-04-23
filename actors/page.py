import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
import pandas as pd
from actors.services import ActorsService

def show_actores():
    actor_service = ActorsService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores:')
        actors_df = pd.json_normalize(actors)#transforma json em um dataframe
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',   
            )
    else:
        st.warning('Nenhum ator encontrado.')

    st.title('Cadastrar novo Ator')
    name = st.text_input('Nome do Ator')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
        )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality= st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,

        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao adastrar o ator. Verificar os campos')
        #st.success(f'Ator {name} cadastrado com sucesso!')