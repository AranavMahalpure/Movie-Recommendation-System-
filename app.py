import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e56fb1e0f1762c91297b69dc687646c7&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
movies_dict= pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie-Recommender-System')
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances= similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:8]
    recommend_movies =[]
    recommended_movie_posters= []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].original_title)
        # fetch poster of the  recommended movies from Api of TMDB
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommended_movie_posters
selected_movie_name= st.selectbox(
    'which movie do you want to watch ',
    movies['original_title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.title(names[0])
        st.image(posters[0])
    with col2:
        st.title(names[1])
        st.image(posters[1])
    with col3:
        st.title(names[2])
        st.image(posters[2])
    with col4:
        st.title(names[3])
        st.image(posters[3])
    with col1:
        st.title(names[4])
        st.image(posters[4])
    with col2:
        st.title(names[5])
        st.image(posters[5])
    with col3:
        st.title(names[6])
        st.image(posters[6])
    with col4:
        st.title(names[7])
        st.image(posters[7])


