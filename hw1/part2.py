# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

count = 0
for title in titles:
    print(f"{count + 1}.", title)
    count+= 1
print("Titles:", len(titles))

countOfA = 0
for title in titles:
    if "a" in title.casefold():
        countOfA+=1
print("Titles with an \"a\":", countOfA)

longest = ""
for title in titles:
    if len(title) > len(longest):
        longest = title
print("Longest:", longest)