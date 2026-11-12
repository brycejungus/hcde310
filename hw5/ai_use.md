**1**. AI was used.
**2**. My Ai use followed the stage listed at the top of the assignment: Stage 5.
**3**. import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json().get("data", [])[:10]

^ api.py

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
    except Exception as e:
        return render_template("home.html", message=f"Something broke the request: {e}")
    return render_template("results.html", artist=artist, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)

^ app.py

Review this Flask app for bugs, missing error handling, accessibility and security problems. For each one, point to the line.

Neither template was included, so I can point to lines only in the two Python files. The accessibility notes at the end are things to check in home.html and results.html. Line numbers count from the first line of each snippet as you pasted it.

Security

app.py line 26: app.run(debug=True). This is the most serious issue. Debug mode turns on the Werkzeug interactive debugger. If an error ever happens while the app is reachable from another machine (for example run with host="0.0.0.0", or deployed like this), anyone who sees the traceback page can run Python on your server. Control it with an environment variable instead:

python
app.run(debug=os.environ.get("FLASK_DEBUG") == "1")

app.py line 21: message=f"Something broke the request: {e}". This shows the raw exception text to the user. A requests error usually includes the full upstream URL, the query string and internal details. Log the details on the server and show a generic message:

python
app.logger.exception("Artwork lookup failed for %r", artist)
return render_template("home.html", message="The art museum's service didn't respond. Please try again."), 502

app.py line 13: methods=["GET", "POST"]. A search changes nothing, so it should be GET only. Accepting POST without CSRF protection does little harm here, but POST results can’t be bookmarked or shared, and pressing back shows a “resubmit form?” prompt. request.values on line 15 also merges the query string and form data, which hides where the input came from. Use request.args with GET.

app.py line 15: no length limit on artist. Any length of string gets passed to the upstream API. Add a reasonable cap, for example reject anything over 100 characters.

XSS (no line yet). Line 22 echoes artist back into the page. Jinja escapes it automatically for .html templates, so this is safe as long as the template doesn’t use {{ artist|safe }} or Markup. The same goes for message and artwork titles.

Bugs

api.py line 8: "q": artist is a full-text search, not an artist filter. Searching “Monet” returns any artwork whose record mentions Monet, which can include works by other artists. Either filter on artist_title in the query, or filter the results in Python:

python
return [a for a in data if artist.lower() in (a.get("artist_title") or "").lower()]

api.py line 12: .json() can raise, and .get assumes a dict. A non-JSON response (an HTML error page from a proxy, say) raises ValueError. JSON that isn’t an object raises AttributeError. The [:10] slice also does nothing extra, since limit=10 on line 8 already caps the results.

api.py line 12: the IIIF base URL and missing images are lost. The API’s response includes a config.iiif_url that you need to build image URLs, and this function drops it. That means the template has to hard-code it. Many artworks also have image_id: null, so the template needs to handle a missing image rather than rendering a broken <img>.

app.py line 20: except Exception is too broad. Catch the failures you expect instead: requests.RequestException (timeouts, connection errors, the 4xx/5xx from line 11) and ValueError (bad JSON). A real bug in your own code then still surfaces during development instead of being reported to the user as a network problem.

app.py lines 17, 21: errors come back with HTTP status 200. Return 400 for an empty search and 502 for an upstream failure, so browsers, tests and any monitoring can tell success from failure.

app.py line 22: no empty-results path. If the search finds nothing, artworks is []. Check that results.html shows a “No artworks found for …” message rather than a blank page.

api.py line 9: identifying header. The Art Institute of Chicago’s API docs ask clients to send an AIC-User-Agent header with a project name and contact email. Setting the standard User-Agent is fine, but adding theirs is the courteous choice.

Accessibility (check in the templates)
Images: every <img> needs meaningful alt text, such as alt="{{ a.title }} by {{ a.artist_title }}". When image_id is missing, show a text placeholder instead of an image.
Search form: the input needs a visible <label for="artist">, not just placeholder text, and the button should say what it does (“Search artworks”).
Error message: put message in an element with role="alert" so screen readers announce it after the page reloads.
Page basics: <html lang="en">, a <title> that includes the search term on the results page (for example “Results for Monet”), and a single <h1>.
Results structure: use a list (<ul>/<li>) or headings for each artwork so screen-reader users can move between them, and make sure the link text makes sense out of context.

If you send home.html and results.html, I can point to exact lines in those too.

1. What is response.raise_for_status() for?
2. What does Exception as e mean?
1. response.raise_for_status()

requests.get() doesn’t treat an error response from the server as a failure. If the API answers with 404 Not Found or 500 Internal Server Error, you still get an ordinary response object and your code keeps running. It would then call .json() on what might be an HTML error page and break in a more confusing place, or quietly show the user no results.

raise_for_status() checks the status code:

2xx (success, e.g. 200 OK): does nothing.
4xx or 5xx (client or server error): raises requests.HTTPError.

So in your api.py, line 11 turns “the server said no” into an exception. That exception travels up to the try/except in app.py, which shows the error message.

python
response = requests.get(URL, ...)   # might come back as 503 Service Unavailable
response.raise_for_status()         # raises HTTPError here if so
return response.json()              # only runs if the status was 2xx
2. except Exception as e

There are two parts:

except Exception means “catch any error of type Exception or any of its subtypes.” Almost every error you’ll meet is a subtype of Exception: HTTPError, ValueError, KeyError, ConnectionError and so on. That’s why this line catches nearly everything.
as e stores the error object in the variable e, so you can use it inside the except block. Turning it into text with str(e) or f"{e}" gives you its message, such as 503 Server Error: Service Unavailable for url: https://....
python
try:
    artworks = get_artworks(artist)
except Exception as e:
    print(type(e).__name__)   # e.g. "HTTPError"
    print(e)                  # e.g. "503 Server Error: ... for url: ..."

My earlier review suggested catching narrower types for this reason. except requests.RequestException as e catches only network and HTTP problems. A typo or other bug in your own code would then still crash loudly during development instead of being shown to the user as “Something broke the request.”

app.py line 20: except Exception is too broad. Catch the failures you expect instead: requests.RequestException (timeouts, connection errors, the 4xx/5xx from line 11) and ValueError (bad JSON). A real bug in your own code then still surfaces during development instead of being reported to the user as a network problem.

give me the code to fix this

Updating the results function in app.py.

Here’s the updated app.py. Only the import requests line and the except line changed:

python
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
    except (requests.RequestException, ValueError) as e:
        return render_template("home.html", message=f"Something broke the request: {e}")
    return render_template("results.html", artist=artist, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)
import requests: app.py needs this to refer to requests.RequestException, even though the actual request is made in api.py.
except (A, B) as e: a tuple catches either type. requests.RequestException covers timeouts, connection failures and the HTTPError from raise_for_status(). ValueError covers .json() failing on a response that isn’t valid JSON.
Anything else now crashes with a normal traceback, such as a typo like artwork.titel in api.py. That’s what you want while developing, because you see the real bug instead of a vague “Something broke” message.

This change still shows {e} to the user. To also fix that issue from the review, log the details and show a plain message:

python
    except (requests.RequestException, ValueError):
        app.logger.exception("Artwork lookup failed for %r", artist)
        return render_template("home.html", message="The art museum's service didn't respond. Please try again."), 502

when i intentionally mess up the api link the raw erroe message is still there

Predicting how the narrowed exception handler will behave.

That’s expected. The last change only fixed which errors get caught. The line that builds the message still puts the raw error text on the page with {e}:

python
message=f"Something broke the request: {e}"

A broken URL raises a requests error, so the except catches it correctly, and then {e} shows its full text. Replace the except block in results() with this:

python
    except (requests.RequestException, ValueError):
        app.logger.exception("Artwork lookup failed for %r", artist)
        return render_template(
            "home.html",
            message="Sorry, we couldn't reach the art museum's service. Please try again.",
        ), 502
No as e and no {e}: the user only ever sees your plain message.
app.logger.exception(...): prints the full error and traceback in the terminal where Flask is running, so you can still see what went wrong while debugging.
, 502: sends a “Bad Gateway” status code. That’s the standard code for “our server is fine, but the service it depends on failed.”

To test it, break the URL again and reload. The page should show the friendly message, and the terminal should show the real error.

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

Your except block is right, but the last line of the function is missing. When the search succeeds, the function now reaches the end without returning anything. Flask then crashes with TypeError: The view function for 'results' did not return a valid response.

Add the success return back after the try/except, at the same indentation as try:

python
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

Also check that import requests is still at the top of app.py. Without it you’d get a NameError the first time an error happens.

To test both paths, run one search with the correct URL (results should appear) and one with the broken URL (you should get the friendly message).

the page is just not loading now

Checking why the page fails to load.

“Not loading” usually means the Flask server stopped, and the terminal where you ran python app.py will say why. Look there first.

1. The terminal shows an error and you’re back at the prompt. In debug mode Flask restarts every time you save. If the saved file has a mistake, the restart fails and the server quits, and the browser then says “This site can’t be reached.” The error to look for is usually near the bottom:

IndentationError or SyntaxError: often a mix of tabs and spaces, or the new return line not lined up with try. Every line directly inside def results(): needs the same 4-space indent.
NameError: name 'requests' is not defined: add import requests at the top of app.py.

Fix the line it names, then run python app.py again. Once the server crashes it doesn’t come back by itself.

2. The browser keeps spinning for a while and then finishes. Your request has timeout=10, so a broken URL that points to a server that never answers can keep the page waiting up to 10 seconds before the friendly message appears. That’s normal. To test the error page faster, break the URL in a way that fails immediately, such as https://api.artic.edu/api/v1/doesnotexist, which returns a 404 straight away.

3. The server is running but no page loads at all. Make sure you’re visiting the address the terminal prints (usually http://127.0.0.1:5000), and that an old copy isn’t still running in another terminal window.

If none of these fit, paste the last 15 or so lines from the terminal and I’ll point to the problem.

**4**. The AI wrote this:
    except (requests.RequestException, ValueError):
        app.logger.exception("Artwork lookup failed for %r", artist)
        return render_template(
            "home.html",
            message="Sorry, we couldn't reach the art museum's service. Please try again.",
        ), 502

This changed the exception as e part and made it so that a message was shown for when artists dont show up, as well api errors. Before, the raw error was just being shown. 


5. Reflection: 
I think working with the AI was a lot better. However, it gave me so much information about all of my bugs and some of them seemed pretty minimal. I think it was nicer to have more freedom with it though. I feel like in the older stages it was annoying because it would keep pestering me to answer a bunch of questions before I could ask another question.