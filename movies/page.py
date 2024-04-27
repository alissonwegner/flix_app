import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
import pandas as pd
from actors.services import ActorsService
from genres.services import GenreService
from movies.services import MovieService

def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='actors_grid',
            )
    else:
        st.warning('Nenhum filme encontrado')

    st.title('Cadastrar novo Filme')
    title = st.text_input('Nome do Filme')
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
        )    
    genre_service = GenreService()#coleta na api todos generos
    genres = genre_service.get_genres()
    genres_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Genero', list(genres_names.keys()))

    actor_service = ActorsService()
    actors = actor_service.get_actors()
    actors_names = {actor['name']: actor['id'] for actor in actors}
    selected_actor_name = st.multiselect('Ator', list(actors_names.keys()))
    selected_actors_ids = [actors_names[name] for name in selected_actor_name]#usado para pegar todos IDs selecionado e enviar para api uma lista
    resume= st.text_area('Resumo')
    

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genres_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao adastrar o ator. Verificar os campos')
        #st.success(f'Ator {name} cadastrado com sucesso!')