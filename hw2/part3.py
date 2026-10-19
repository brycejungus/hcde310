# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

artistWorks = {}
for piece in artworks:
    artist = piece.get("artist", "Unknown")
    if artist in artistWorks:
        artistWorks[artist] += 1
    else:
        artistWorks[artist] = 1
print(artistWorks)

topArtist = max(artistWorks, key=artistWorks.get)
mostWorks = artistWorks[topArtist]
print("Most works:", topArtist, f"({mostWorks})")
