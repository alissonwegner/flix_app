## Aplicação de Frontend para Site de Filmes com Streamlit

Este projeto consiste em uma aplicação de frontend desenvolvida em Python utilizando o framework Streamlit para criar um site de filmes que consome dados de uma API pública de filmes, como o TMDb (The Movie Database). A aplicação exibe informações sobre filmes populares e permite visualizar detalhes de cada filme selecionado.

### Funcionalidades Principais

- **Listagem de Filmes Populares:** A aplicação obtém uma lista de filmes populares através de uma requisição para a API do TMDb.
  
- **Seleção e Visualização de Detalhes:** Os filmes são exibidos em uma lista suspensa, permitindo ao usuário selecionar um filme para visualizar mais detalhes, como título, data de lançamento, resumo, classificação média e pôster.

### Requisitos

- Python 3.x
- Streamlit
- Requests

### Como Usar

1. **Instalação das Dependências:**
   Certifique-se de ter Python instalado. Instale as dependências necessárias executando o seguinte comando:
- python3 -m venv venv
-  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
-  .\venv\Scripts\activate 
-  pip install streamlit  
-   pip install streamlit-aggrid
-    pip install streamlit requests
-    streamlit run app.py   
