import streamlit as st
import plotly.express as px
from movies.services import MovieService 

def show_home():
   movie_service = MovieService()
   movie_stats = movie_service.get_movie_stats()
   st.title('Estatisticas de filmes')

   if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)  

   st.subheader('total de filmes cadastrados:')
   st.write(movie_stats['total_movies'])

   st.subheader('total de avaliações cadastradas:')
   st.write(movie_stats['total_reviews'])

   st.subheader('Media geral de estrelas nas avaliações:')
   st.write(movie_stats['average_stars'])
