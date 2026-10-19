# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
Artworks is a list of dictionaries because it allows each artwork to have its own distinguishable data. If it was one big dictionary, it would be really fast to look items up, but every item would need a unique key. With the list of dictionaries, you have every list as it's own art work so there's no conflict with keys.

## 2. Which fields are sometimes missing? What should the app show when they are?
Sometimes the medium, artist, and year don't show. The app should show a message like "field missing" or "field not found" when it's not there. When they are there, it should show the label with the corresponding art work. 