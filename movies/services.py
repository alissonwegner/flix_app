import streamlit as st
from movies.repository import MoviesRepository


class MoviesService:

    def __init__(self):
        self.movie_repository = MoviesRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()
    
    def create_movie(self,title, genre, release_date, actors, resume):
        movie = dict(
            title=title,
            genre=genre,
            release_date=release_date,
            actors=actors,
            resume=resume,

        )
        return self.movie_repository.create_movie(movie)