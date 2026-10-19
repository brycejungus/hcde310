# HW2 Part 4 – Your first functions
#
# In `part4.py`, turn code you already wrote into functions:
#
# 1. `works_by(artist, artworks)` → returns a list of titles by that artist, from the list you pass in
#    (an empty list if there are none)
# 2. `count_by_artist(artworks)` → returns your counting dictionary from Part 3
# 3. Replace each `TODO` docstring with one line saying what the function takes and what it returns
#
# Don't change the `print` lines at the bottom of `part4.py`. `check.py` uses them.

from artworks import artworks


def works_by(artist, artworks):
    """It takes a specifc artist, a list of artworks, and returns the list of artworks that the artist passed in made."""
    works = []
    for piece in artworks:
        if piece.get("artist") == artist:
            works.append(piece.get("title"))
    pass
    return works

def count_by_artist(artworks):
    """The function takes in a list of artworks and returns the number of artworks each artist in the list did."""
    artistWorks = {}
    for piece in artworks:
        artist = piece.get("artist", "Unknown")
        if artist in artistWorks:
            artistWorks[artist] += 1
        else:
            artistWorks[artist] = 1
    pass
    return artistWorks


print(works_by("Claude Monet", artworks))
print(works_by("Nobody", artworks))
print(count_by_artist(artworks))
