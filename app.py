from flask import Flask, request, render_template, jsonify
# from flask_caching import Cache

from src.book_scraper import BookScraper

"""
Mounts a prefix for all routes
"""
SCRIPT_NAME = "/api"

"""
Scraper for book API
"""
SCRAPER = BookScraper("")

"""
The main application
"""
app = Flask(__name__)

@app.route("/books")
def get_books():
    results = SCRAPER.scrape()

    accepts = request.headers.get("Accept")
    match accepts:
        case "text/html":
            return render_template("books.html", results)
        case _:
            return jsonify(results)