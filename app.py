import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6c6a4d6eea269d143babcc1d60f89af0&&language-en-US'.format(movie_id))
    data = response.json()


    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]
    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        movies_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies_id))

    return recommended_movies,recommended_movies_poster

st.set_page_config(layout="wide")
st.title('movie recommender system')
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
option = st.selectbox('How would you like to continue?',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(option)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])