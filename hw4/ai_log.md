I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: [name]([inputs]) takes [what] and returns [what].
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Your routine looks good, and I’m ready to follow it. Your message still has the template placeholders in it, though, so I don’t have your problem yet. Can you fill these in?

My attempt so far: paste your code or plan, even if it doesn’t work. A rough sketch in plain English is fine too.
Where I’m stuck: one sentence.
The function I need: name(inputs) takes ___ and returns ___.
Libraries you’re already using, if any (for example tkinter, streamlit or pygame). This keeps me to tools you already know.

It would also help to have one real example input you expect to pass in, since that’s what I’ll ask you to predict the output for.

Once you send these, I’ll write only the function (marked # AI-written and with a one-line docstring), then stop and ask for your prediction.

def search_art(term):
    params = {"q":term, "fields":FIELDS} 
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.RequestException:
        print("API error: no answer") 
        return None

    if (response.status_code != 200):
        print(response.status_code, response.reason)
        exit()
    data = response.json()

I'm getting an error and flask won't start up for this. I've tried looking at the response code

Diagnosing why the Flask app won't start.

You haven’t given me a function signature yet, so I’ll stay in tutor mode for now: hints and questions, no code.

The most useful clue is the error message itself. When Flask fails to start, the terminal prints a traceback. Can you paste the last 5–10 lines, especially the final line (something like NameError: ... or ModuleNotFoundError: ...)?

While you find that, here are some things to think about:

When does this code actually run? Defining a function doesn’t run its body. Python only runs the body when something calls search_art(...). If Flask crashes at startup, before you’ve visited any page, is the response-code check even running yet? Look at the line number in the traceback. Is it inside this function, or somewhere else?
Where do url, headers, FIELDS and requests come from? Your function uses all four but creates none of them. Find where each one is defined or imported in your file.
What does exit() do in a web server? Compare it with the except block just above it. What does that block do differently when something goes wrong, and why might that be better inside a Flask app?
What does the function give back when everything works? Follow the success path to the last line. What does the code that called search_art actually receive?

Send me the traceback and your answer to #1, and we’ll go from there. If you find you need a helper function written, tell me its name, its inputs and what it returns, and I’ll follow your routine.

Here’s the replacement for the line inside your <li>. Templates don’t have docstrings, so I’ve put the one-line description in the Jinja comment instead.

html
{# AI-written: takes art.title and shows "Untitled" if it's missing, empty, or None #}
<li>{{ art.title | default("Untitled", true) }}</li>

Predict before you run it. Suppose your API returns these three artworks:

python
[{"title": "The Bedroom"}, {"title": ""}, {"artist": "Hokusai"}]

What will each of the three bullets show on the page? Write down your guesses, then tell me.

i think the first one will show bedroom, the second will show untitled, and the third one will show untitled as well

Your prediction is logged:

“Bedroom”
“Untitled”
“Untitled”

Now run it. Search for something in your app, or temporarily pass that test list to results.html from your route. Then tell me exactly what the three bullets show, word for word.

While you look, watch the first bullet closely and see whether it matches your guess exactly.


i forgot to add a way to show more than just the title. can you make that for me to put into results.html? 

here's the code for it right now
<!doctype html>
<html lang="en">
<head><title>Art relevant to {{ term }}</title></head>
<body>
  <h1>Art relevant to {{ term }}</h1>
  <ul>
  {% for art in artworks %}
    <li>{{ art.title }}</li>
    {# AI-written: takes art.title and shows "Untitled" if it's missing, empty, or None #}
    <li>{{ art.title | default("Untitled", true) }}</li>
  {% endfor %}
  </ul>
  <a href="/">New search</a>
</body>
</html>

I can write that, but I need two things from you first.

1. Which fields do you want to show? Paste the line where you set FIELDS in api.py. Your template can only show fields the API actually sends back, and I’d only be guessing at the names (for example artist_title vs. artist).

2. Close out the last step. You haven’t told me what happened when you ran it. Looking at the template you just pasted, how many <li> lines are inside the loop now? What do you think each artwork will look like on the page because of that? Run it, and tell me what the three bullets showed and whether they matched your prediction.

Once I have your FIELDS line, I’ll write the new piece and ask you to predict it, the same as before.

i want to show artist_display and date_display

Deciding whether earlier routine steps should be enforced.
Deciding whether earlier routine steps should be enforced.
Here’s the replacement for your AI-written <li>, the one that uses default. Keep the comment line above it.

html
{# AI-written: takes an artwork and shows its title, artist, and date, with a fallback for each if missing #}
<li>
  <strong>{{ art.title | default("Untitled", true) }}</strong><br>
  {{ art.artist_display | default("Unknown artist", true) }}<br>
  {{ art.date_display | default("Date unknown", true) }}
</li>
Two HTML tags you may not have used yet:

<strong> makes the text inside it bold.
<br> starts a new line inside the same bullet.
Predict: what will the page show for this artwork?

python
{"title": "The Great Wave", "artist_display": "", "date_display": "1831"}
Write out what you think the bullet looks like, line by line. Also keep in mind that your loop still has your original <li>{{ art.title }}</li> line above this one. When you run it, notice what that line adds to each artwork, then tell me your prediction and what actually showed up.


What surprised me is how many connecting parts there is to make a working web app, even at this small of scale.

I had to change a lot from the templates on my own, but they were a good starting point. I think it was pretty similar but still a little difficult. I used the book search template, so changing a lot of the variables from that to artist is mainly what I changed. 