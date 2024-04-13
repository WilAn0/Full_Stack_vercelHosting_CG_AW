from fastapi import APIRouter
import database
from queries import tartare as queries

app = APIRouter()


@app.get("/reviews")
def get_reviews_by_movie(movie_name: str):
    query = queries.movie_review_query

    reviews = database.execute_sql_query(query, (movie_name,))
    if isinstance(reviews, Exception):
        return reviews, 500
    reviews_to_return = []
    for review in reviews:
        review_dictionary = {
            "MovieName": review[0],
            "Review": review[1],
            "Stars": review[2]
        }
        reviews_to_return.append(review_dictionary)
    return {'reviews': reviews_to_return}

@app.get("/movietest")
def get_all_movies():
    query = queries.movie_test_query
    movies = database.execute_sql_query(query)
    if isinstance(movies, Exception):
        return movies, 500
    movies_to_return = []
    for movie in movies:
        movies_to_return.append(movie[0])
    return {'movies': movies_to_return}


@app.get("/info")
def get_reviews_by_movie(movie_name: str):
    query = queries.movie_details_query

    movies = database.execute_sql_query(query, (movie_name,))
    if isinstance(movies, Exception):
        return movies, 500

    movies_to_return = []
    for movie in movies:
        movie_dictionary = {
            "Movie": movie[0],
            "Synopsis": movie[1],
            "Duration": movie[2],
            "Country": movie[3],
            "Genre": movie[4],
            "Actor1": movie[5],
            "Actor2": movie[6],
            "Actor3": movie[7],
            "Actor4": movie[8],
            "Actor5": movie[9],
            "Actor6": movie[10],
            "Director": movie[11]

        }
        movies_to_return.append(movie_dictionary)
    return ({'movies': movies_to_return})




