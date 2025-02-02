# Movie Recommender System

A sophisticated content-based movie recommender system built using TMDB dataset and cosine similarity algorithm.

## 🎯 Overview

This project is a web-based application that recommends similar movies based on user selection. It uses content-based filtering to analyze movie features and suggest films that share similar characteristics with the user's chosen movie.

## ✨ Features

- Interactive web interface built with Streamlit
- Movie search functionality with dropdown selection
- Display of movie posters using TMDB API
- Recommendations based on content similarity
- Error handling and fallback mechanisms
- Responsive design showing 5 movie recommendations

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- scikit-learn (for cosine similarity)
- TMDB API
- Pickle (for model serialization)
- Requests (for API handling)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/IvanNilash1206/movie-recommender-system.git
cd movie-recommender-system
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up TMDB API:
   - Get an API key from [TMDB website](https://www.themoviedb.org/documentation/api)
   - Replace the API key in `app.py`

## 🚀 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`
3. Select a movie from the dropdown menu
4. Click "Show Recommendation" to see similar movies

## 🗄️ Project Structure

- `app.py`: Main application file with Streamlit interface
- `movie_list.pkl`: Preprocessed movie data
- `similarity.pkl`: Pre-computed similarity scores
- `requirements.txt`: Project dependencies

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/IvanNilash1206/movie-recommender-system/issues).

## 👨‍💻 Author

Ivan Nilash
- GitHub: [@IvanNilash1206](https://github.com/IvanNilash1206)

## 🙏 Acknowledgments

- TMDB for providing the movie database API
- Streamlit for the awesome web framework
- The open-source community for various tools and libraries used
