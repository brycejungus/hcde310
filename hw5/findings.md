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
What was wrong: When there was an error, specifically with the API, the raw error message would appear. 
What I changed: I changed it so that if there's an error with the API, then the raw error message wouldn't show and a message saying "Sorry, we couldn't reach the art museum's service. Please try again." would show. 
How I checked it works: I ran the app and changed the API's URL by deleting two words and saw the error message.
Commit before: (hash) commit 5efe03a26d138a7959ffac15c628a1852ba21064  
Commit after: (hash) commit 6cd383ccde64a68714759b0a310d6ae70e8cb400

## 6. Can we ship it? (100–150 words)
Yes or no, and why: No, I don't think we could ship this tomorrow. The app's UI is very basic and simple. It's also not very acessible and still pretty raw. I think for a mini class assignment it's fine, but for a product to be shipped it has to look way better. I also think that it doesn't always function very well. The images don't show up on my end which is the main point of this app. For it to be shipped, I think the main functionalities would have to be fixed first, then make the app look better and accessible. 

One thing my HW4 does better: The images actually appear after the search is shown.
One thing the AI's app does better: The error messages are a little better? Not much is better to be honest.

AI use goes in `ai_use.md` (the five points on the AI Use Card).
