# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

for i in range(len(years)):
    year = years[i]
    if year > cutoff:
        print(titles[i])

print()
for i in range(len(years)):
    title = titles[i]
    year = years[i]
    if year > cutoff:
        print(f"{title}: modern")
    else:
        print(f"{title}: old")

print()
oldNum = 0
modernNum = 0
for i in range(len(years)):
    title = titles[i]
    year = years[i]
    if year > cutoff:
        modernNum += 1
    else: 
        oldNum += 1
print("Old:", oldNum)
print("Modern:", modernNum)