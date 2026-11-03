![Picture of sketch](<Untitled (Draft)-4.jpg>)


#app.py
#needs flask, render_template, request

#SPECS 

# route for '/'
# input: user types '/' into url bar
# output: home.html template

# route for 'results'
# input: user presses Submit from home.html template and flask gets the term
# output: ideal path is that results.html pulls up with results from successful api call

# errors or states:
# empty: return to home.html and put message "Please enter in search term"
# no results: return to home.html and put message "No results found"
# api error: return to home.html and put message "Something went wrong." With a generic message
# missing fields: if all fields are empty return home.html with message "Untitled". If non-empty fields, return results.html.

# api.py: calls for art
# needs requests library, url, and search term

# use function from HW3 

# errors:
# if status code is not 200, print what the status code is



Checks:
* / page loads, text appearing as normal
* /results: "monet" shows results, empty search shows message, nonsense input shows message
* search_art: a broken URL shows error message and doesn't crash. 

^ All checked