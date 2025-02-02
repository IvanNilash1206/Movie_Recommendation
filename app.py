import pickle
import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def fetch_poster(movie_id):
    try:
        # Configure more robust retry strategy
        session = requests.Session()
        retries = Retry(
            total=5,  # Increased total retries
            backoff_factor=0.5,  # Reduced backoff time
            status_forcelist=[500, 502, 503, 504, 429],  # Added 429 (Too Many Requests)
            allowed_methods=["HEAD", "GET", "OPTIONS"]  # Explicitly specify allowed methods
        )
        adapter = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=10)
        session.mount('https://', adapter)
        
        url = "https://api.themoviedb.org/3/movie/{}?api_key=7c55741dad1721124a578162176cc4a8&language=en-US".format(movie_id)#Replace API HERE
        data = session.get(url, timeout=(3.05, 27))  # Connect timeout of 3.05s, Read timeout of 27s
        data.raise_for_status()
        data = data.json()
        
        if 'poster_path' not in data or data['poster_path'] is None:
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
            
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except (requests.exceptions.RequestException, ConnectionResetError, ProtocolError) as e:
        st.error(f"Error fetching poster: {str(e)}")
        return "https://via.placeholder.com/500x750.png?text=Error+Loading+Poster"
    except KeyError as e:
        st.error(f"Error processing movie data: {str(e)}")
        return "https://via.placeholder.com/500x750.png?text=Error+Processing+Data"

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters
    except IndexError:
        st.error(f"Movie '{movie}' not found in the database.")
        return [], []


st.header('Movie Recommender System')
try:
    movies = pickle.load(open('movie_list.pkl','rb'))
    similarity = pickle.load(open('similarity.pkl','rb'))
except FileNotFoundError:
    st.error("Required model file not found")
    st.stop()
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names and recommended_movie_posters:  # Only show recommendations if we have results
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])





