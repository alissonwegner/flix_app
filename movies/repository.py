import requests
import streamlit as st
from login.services import logout

class MoviesRepository:
    
    def __init__(self):
        self.__base_url = 'http://192.168.101.73:8000/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    

    def create_movie(self, movies):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movies,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')