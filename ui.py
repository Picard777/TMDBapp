from rich.console import Console
from rich.table import Table

console = Console()

def rate_style(value):
    if value is None:
        return "dim"
    
    try:
        value = float(value)
    except ValueError:
        return "dim"
    
    if value >= 7.5:
        return "bold green"
    elif value >=6.0:
        return "yellow"
    else:
        return "red"
    
        
def show_commands():
    table = Table(title="TMDB CLI COMMANDS", header_style = "bold magenta")
    table.add_column("Command", style="blue cyan")
    table.add_column("Description", style="white")
    
    table.add_row("now-playing", "Show movies now playing in theaters")
    table.add_row("popular", "Show popular movies")
    table.add_row("top-rated", "Show top rated movies")
    table.add_row("search", "Search for a movie")
    
    console.print(table)  

def show_movies(title: str, movies: list):
    table = Table(
        title = title, 
        show_lines = True,
        style="green",
        header_style = "bold magenta"
    )
    
    table.add_column("#", justify="right", style="bold magenta")
    table.add_column("Title", style="bold cyan", no_wrap=True)
    table.add_column("Year", justify="center", style="white")
    table.add_column("Rating", justify="right", style="white")
    table.add_column("Overview", overflow="fold", style="white")
    
    
    for i, movie in enumerate(movies, start=1):
        rating = movie.get("vote_average")
        
        table.add_row(
            str(i),
            movie.get("title", "N/A"),
            movie.get("release_date", "")[:4],
            f"[{rate_style(rating)}]{rating if rating else "N/A"}[/]",
            movie.get("overview", "No description") + "-"
        )
    
    console.print(table)
    