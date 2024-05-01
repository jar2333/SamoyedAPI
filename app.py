from flask import Flask, request, render_template, jsonify
from flask_caching import Cache

from env import GOODREADS_URL

from src.book_scraper import BookScraper

"""
Mounts a prefix for all routes
"""
SCRIPT_NAME = "/api"

"""
Scraper for book API
"""
SCRAPER = BookScraper(GOODREADS_URL)

"""
App configuration
"""
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

"""
The main application
"""
app = Flask(__name__)
app.config.from_mapping(config)

cache = Cache(app)

@app.route("/books")
@cache.cached(timeout=86400)
def get_books():
    results = SCRAPER.scrape()
    return render_template("books.html", results), 200