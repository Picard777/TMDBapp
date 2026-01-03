import requests
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def fetch(endpoint, params=None):
    params=params or {}
    params["api_key"] = api_key
    
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

def now_playing():
    return fetch("/movie/now_playing")["results"]

def top_rated():
    return fetch("/movie/top_rated")["results"]

def popular():
    return fetch("/movie/popular")["results"]

def search_movie(query):
    return fetch("/search/movie", {"query": query})["results"]

def get_movie_details(movie_id):
    return fetch(f"/movie/{movie_id}")

GENRES = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "sci-fi": 878,
}

def discover_movies(
    query=None,
    year=None,
    genre=None,
    min_rating=None,
    language=None,
    person=None,
    page=1,
):
    params = {"page": page,
              "sort_by": "popularity.desc"}
    if year:
        params["primary_release_date.gte"] = f"{year}-01-01"
        params["primary_release_date.lte"] = f"{year}-12-31"
    if genre:
        params["with_genres"] = genre
    if min_rating:
        params["vote_average.gte"] = min_rating
    if language:
        params["with_original_language"] = language
    if person:
        person_data = find_person(person)
        if not person_data:
            return {"results": [], "page": 1, "total_pages": 0}
        
        person_id = person_data["id"]
        department = person_data["known_for_department"]
        
        if department == "Acting":
            params["with_cast"] = person_id
        else:
            params["with_crew"] = person_id
    return fetch("/discover/movie", params=params)

def movies_by_person(person_name, page=1):
    person = find_person(person_name)
    if not person:
        return {"results": [], "page": 1, "total_pages": 0}
    
    params = {
        "page": page,
        "sort_by": "popularity.desc",
        "include_adult": False,
    }
    person_id = person["id"]
    department = person["known_for_department"]
    if department == "Acting":
        params["with_cast"] = person_id
    else:
        params["with_crew"] = person_id
    return fetch("/discover/movie", params=params)

def find_person(name):
    data = fetch("/search/person", {"query": name})
    results = data.get("results", [])
    
    if not results:
        return None

    return results[0]
