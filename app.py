import streamlit as st
from genres.page import show_genres
from actors.page import show_actores
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews
from home.page import show_home


if 'key' not in st.session_state:
    st.session_state.key = None

def main():
    if 'token' not in st.session_state:
        show_login()

    else:
        st.title('Flix App')
        
        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Inicio', 'Generos', 'Atores', 'Filmes', 'Avaliações']

        )
        if menu_option == 'Inicio':
            show_home()

        if menu_option == 'Generos':
            show_genres()

        if menu_option == 'Atores':
            show_actores()

        if menu_option == 'Filmes':
            show_movies()
             

        if menu_option == 'Avaliações':
            st.write('Lista de Filmes')
            show_reviews()

if __name__ =='__main__':
    main()