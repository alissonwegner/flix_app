import streamlit as st
from api.services import Auth
import requests

def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )
    if response.get('error'):
        st.error(f'falha ao realizar o login: {response.get("error")}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()
    #st.rerun() refresh na tela

def logout():
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()