import requests
from flask import Flask, render_template, request

from api import get_artworks

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    artist = (request.values.get("artist") or "").strip()
    if not artist:
        return render_template("home.html", message="No search term entered.")
    try:
        artworks = get_artworks(artist)
    except (requests.RequestException, ValueError):
        app.logger.exception("Artwork lookup failed for %r", artist)
        return render_template(
            "home.html",
            message="Sorry, we couldn't reach the art museum's service. Please try again.",
        ), 502
    return render_template("results.html", artist=artist, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)
