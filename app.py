import pickle
import streamlit as st
import requests
import pickle
import os





def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
file_path = os.path.abspath('movie_list.pkl')

# Load the data from the file
with open(file_path, 'rb') as file:
    movies = pickle.load(file)
file_path = os.path.abspath('similarity.pkl')

# Load the data from the file
with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)
#movies = pickle.load(open(r'C:\Users\raali\OneDrive\Desktop\ML projects\movie recommender system\movie_list.pkl','rb'))
#similarity = pickle.load(open(r'C:\Users\raali\OneDrive\Desktop\ML projects\movie recommender system\similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    columns = st.columns(5)
    for i in range(5):
        with columns[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])








