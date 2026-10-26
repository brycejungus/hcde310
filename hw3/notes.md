# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
'data["data"][0]["title"]'

## 2. Find 3 more fields you'd want to show a user, and their paths
date_display: data["data"][0]["date_display"]
artist_display: data["data][0]["artist_display"]
medium_display: data["data"]["medium_display"]

## 3. Which fields are `null` for some works?
artist_title and preference

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think there will be an error or nothing will happen at the very least because there's nothing in url or params.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
So there is no valid URL so there was nothing to fetch a result from resulting in an error. The line that caused it was line 16 when the response is called to get the request from the url.