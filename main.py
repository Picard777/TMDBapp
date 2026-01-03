import argparse
from tmdb import now_playing, popular, top_rated, search_movie, discover_movies, movies_by_person, GENRES
import textwrap
from ui import show_movies
from ui import show_commands


def print_movies(movies):
    for idx, movie in enumerate(movies, start=1):
        title = movie.get("title")
        release = movie.get("release_date")
        rating = movie.get("vote_average")
        overview = textwrap.shorten(
            movie.get("overview", "No description available"),
            width=80,
            placeholder = "..."
            )
        print(f"{idx}. {title} ({release} ⭐ ({rating}))")
        print(f" {overview}\n")

def main():
    parser = argparse.ArgumentParser(
        description="TMDB Movie CLI"
    )
    
    subparsers = parser.add_subparsers(dest="command")
    
    #now_playing
    subparsers.add_parser("now-playing", help="Show movies now playing in theaters")
    
    #popular
    subparsers.add_parser("popular", help="Show movies that are popular now")
    
    #top_rated
    subparsers.add_parser("top-rated", help="Show top rated movies")
    
    #search
    search = subparsers.add_parser("search", help="Search a movie")
    search.add_argument("query", nargs="?", help="Movie title (optional)")
    search.add_argument("--year", type=int, help="Filter results by release year")
    search.add_argument("--genre", help="Filter results by genre", choices=GENRES.keys())
    search.add_argument("--min-rating", type=float, help="Filter results by minimum rating")
    search.add_argument("--language", help="Filter results by language")
    search.add_argument("--page", type=int, default=1, help="Page number for results pagination")
    search.add_argument("--person", help="Filter results by person (actor/director)")

    args = parser.parse_args()
    
    if args.command is None:
        show_commands()
        return
    
    if args.command == "now-playing":
        print("\nNOW PLAYING\n" + '-' * 50)
        show_movies("Now Playing", now_playing())
    elif args.command == "popular":
        print("\nPOPULAR MOVIES\n" + "-" * 50)
        show_movies("Popular Movies", popular())
    elif args.command == "top-rated":
        print("\nTOP RATED MOVIES\n" + "-" * 50)
        show_movies("Top Rated", top_rated())
    elif args.command == "search":
        genre_id = GENRES.get(args.genre) if args.genre else None
        filters_used = any([
            args.year,
            genre_id,
            args.min_rating,
            args.language,
        ])
        if args.person and not filters_used and not args.query:
            data = movies_by_person(args.person, page=args.page)
            show_movies(f"{args.person}", data["results"])
            return
        if args.query and not filters_used:
            data = search_movie(args.query)
            show_movies(f"Search: {args.query}", data)
            return
        if filters_used:
            data = discover_movies(
                year=args.year,
                genre=genre_id,
                min_rating=args.min_rating,
                language=args.language,
                person=args.person,
                page=args.page,
          )
            label = args.query or "Filters"
            show_movies(f"Search: {label}", data["results"])
            return
    else:
        
        parser.print_help()
if __name__ == "__main__":
    main()
    

    



