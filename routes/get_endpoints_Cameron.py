from fastapi import APIRouter
import database
from queries import tartare as queries

app = APIRouter()


@app.get("/contactus")
def get_contactus():
    query = queries.contact_us_query
    contacts = database.execute_sql_query(query)
    if isinstance(contacts, Exception):
        return contacts, 500
    contacts_to_return = []
    for contact in contacts:
        contacts_to_return.append(contact)
    return ({"contacts": contacts_to_return})


@app.get("/movies")
def get_movies():
    query = queries.movie_info_query
    movies = database.execute_sql_query(query)
    if isinstance(movies, Exception):
        return movies, 500
    movies_to_return = []
    for movie in movies:
        movies_to_return.append(movie)
    return ({"movies": movies})


@app.get("/playtime")
def get_playtimes(nowseenmovieid: int):
    query = queries.movie_playtime_query
    playtimes = database.execute_sql_query(query,(
        nowseenmovieid,
    ))
    if isinstance(playtimes, Exception):
        return playtimes, 500
    playtimes_to_return = []
    for playtime in playtimes:
        playtimes_to_return.append(playtime)
    return ({"playtime": playtimes_to_return})