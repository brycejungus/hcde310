# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)


term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q":term, "fields":FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent": "HCDE 310 student project"}
response = requests.get(url, params=params, headers=headers)

# TODO step 3: check response.status_code before you use the data
if (response.status_code != 200):
    print(response.status_code, response.reason)
    exit()
data = response.json()

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results
def count_by_artist(artworks):
    """The function takes in a list of artworks and returns the number of artworks each artist in the list did."""
    artistWorks = {}
    for piece in artworks:
        artist = piece.get("artist_title", "Unknown")
        if artist is None:
            artist = "Unknown"
        if artist in artistWorks:
            artistWorks[artist] += 1
        else:
            artistWorks[artist] = 1
    pass
    return artistWorks


def save_results(artworks, filename):
    """Takes a list of artwork dictionaries and a filename, writes one line per artwork to that text file, and returns how many it wrote."""
    count = 0
    with open(filename, "w") as file:
        for art in artworks:
            title = str(art.get("title", "Unknown"))
            artist = str(art.get("artist_title", "Unknown"))
            date = str(art.get("date_display", "Unknown"))
            file.write(title + " | " + artist + " | " + date + "\n")
            count = count + 1
    return count

results = data["data"]
if len(results) == 0:
    print("No results found")
else:
    for art in results:
        print(art.get("title", "Unknown"), "-", art.get("artist_display", "Unknown"), art.get("date_display"), f"({art.get("year", "Unknown")})")
    termfileName = term + ".txt"
    count = save_results(results, termfileName)
    print(f"Saved {count} artworks to results.txt")





