import pickle

import pandas as pd
import requests
import streamlit as st

#
# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/movie/{"
#                             "}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pickle','rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox(
'Show Recommendations',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    #
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
