# TMDB Movie CLI 🎬

Command-line interface (CLI) application for browsing and searching movies using the TMDB (The Movie Database) API.

This project allows you to explore movies directly from the terminal with rich tables, filters, and search capabilities.

---

## Features

Browse movie lists:
  - Now Playing
  - Popular
  - Top Rated
  - Search movies by title
  - Filter by actor or director
  - Filter by release year
  - Filter by genre (e.g. sci-fi, drama, action)
  - Filter by minimum rating
  - Filter by original language
  - Combine multiple filters (cross-filtering)
  - Beautiful terminal tables powered by `rich`
  - Secure API key handling via `.env`

---

## Requirements

- Python **3.10+**
- TMDB API key (free)

---

## Installation

Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/tmdb-cli.git
cd tmdb-cli

python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```
## Usage
```
python main.py
python main.py now-playing
python main.py popular
python main.py top-rated

python main.py search "Inception"
python main.py search --year 2010
python main.py search --genre sci-fi
python main.py search --min-rating 8
python main.py search --language en
```
## Project structure
TMDBapp/
│
├── main.py        # CLI entry point & argument parsing
├── tmdb.py        # TMDB API communication layer
├── ui.py          # Rich-based terminal UI
├── README.md
├── .gitignore
└── .env           # API key (not committed)

## License
This project is for educational and portfolio purposes.
TMDB data is provided by The Movie Database API.
