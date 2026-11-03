from flask import Flask, render_template, request   # request (Flask), not requests!
from api import search_art


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    term = request.args.get("term_search", "").strip()
    # Checked in browser. I checked with both artist name and just a term. Both produce relevant pieces to the term.
    # This route is results and the term gets the search term from the html form.

    # 2. Empty input? → home page + message (check BEFORE calling the API)
    if not term:
        return render_template("home.html", message="Please enter in search term")
    # The route basically pulls up results. This check sees if there's no term, and then if there isn't it knows that 
    # the search term is empty and returns back to home page with the error message telling the user to enter in a search term.
    # 3. Call the API
    artworks = search_art(term)

    # 4. API error?
    # If nothing is returned for artworks, then the generic message is printed. Something should be returned
    # for artworks every time even if it's no results unless it's an API error.
    if artworks is None:
        return render_template("home.html", message="Something went wrong. Please try again in a moment.")
    # 5. No results, or nothing useful to show? → home page + message
    if len(artworks) == 0:
        return render_template("home.html", message="No art found. Please try again")
    # If no results, aka the artworks is equal to 0, then the message no art is found.
    # 6. Otherwise → results page
    return render_template("results.html", artworks=artworks, term=term)


