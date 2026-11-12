# HW5 findings

## 1. Drawing: one search for "Monet"
(photo here)

![alt text](<Untitled (Draft)-6.jpg>)

## 2. Two questions about the code
1. What is response.raise_for_status() for?
2. What does Exception as e mean?

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | def test_empty_search_shows_message()| pass |
| 2 | def test_home_has_search_button()| pass |
| 3 | # search for mumbo jumbo (kdjfkdjl), get message like "no results found"| fail|
| 4 |# change api link, get error | pass|

## 4. AI review
What it found that I missed: For security wise, it said that app.run(debug=True) makes it so that anyone who sees the traceback page can run Python on my server. It also said that message=f"Something broke the request: {e} shows the raw error to the user. It also says that lines errors come back with HTTP status 200. 
What it got wrong: It said that I needed to put alt text for the images, but that's already there. 
Answers to my two questions, in my own words: 
1. It checks the status code and raises the error if applicable. 
2. It basically means that any error will be caught and then stored in e.
## 5. My fix
What was wrong:
What I changed:
How I checked it works:
Commit before: (hash)  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
