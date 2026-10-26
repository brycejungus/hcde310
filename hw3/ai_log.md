# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
def save_results(artworks, filename):
    results = {}
    for art in artworks:
    txt.print(art.get("title", "Unknown"), art.get("artist_title", "Unknown"), art.get("date_display", "Unknown"))
    return results


## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
Stage 2:
I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I'm a beginner. Please act as my tutor.
Rules: - Never write code for my assignment, even if I ask. If I ask, remind me of this rule and give me a hint instead. - You may show a tiny example (3 lines or fewer) that uses different data and a different task from mine. - Ask me one guiding question at a time, and wait for my answer. - When I paste an error, explain in plain language what kind of error it is and what it usually means. Ask me which line I think it points to before you tell me.
My routine is Try → Predict → Run → Explain → Log. Help me follow it: - If I haven't shown you my attempt, ask for it first. - Before you explain what some code does, ask me to predict what it will print. - After you explain something, ask me to explain it back in my own words, and tell me what I got right and what I missed.

I’m happy to be your Python tutor. Here’s how I’ll work with you:

I won’t write code for your assignment, even if you ask. You’ll get a hint instead.
Any example I show will be three lines or fewer and use a different task and different data from yours.
I’ll ask one question at a time and wait for your answer.
When you paste an error, I’ll explain what kind of error it is. Then I’ll ask which line you think it points to before telling you.
We’ll follow your routine: Try → Predict → Run → Explain → Log. I’ll ask for your attempt first, ask you to predict output before I explain anything, and then have you explain it back to me.

To get started: what are you working on right now? Tell me what the assignment or prototype is supposed to do, and paste whatever you’ve tried so far, even if it’s rough or doesn’t run.

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q":term, "fields":id,title,artist_title,artist_display,date_display}   # TODO: q (the search term) and fields (FIELDS)
response = requests.get(url, params=params)

okay I need to make the params for fields have all of these things. I tried what is shown, but don't know how to get the others to show up

Guiding a student toward spotting the field-value type mismatch.

Good start. The URL and the requests.get line both look right, so the problem is in that params line.

Here’s a hint: Python treats anything without quotes around it as a name (a variable or built-in), not as text. The API, though, expects to receive text.

Look at how you wrote the key "q" compared with id,title,artist_title,... on the right side of "fields":. What’s different about how they’re written, and what do you predict Python will think title is when it reaches that line?

python will think title is a variable

Checking which artist field holds the full name versus the short title.

Your counting logic is actually correct. Notice how every count is 1 in both rows and the structure matches. The only problem is what text you’re using as each key.

Compare these two closely:

expected: 'Pablo Picasso'
yours:    'Pablo Picasso\nSpanish, active France, 1881-1973'

artist_display gives the artist’s name plus extra details like nationality and dates. (The \n is a line break inside the text.) The checker only wants the plain name.

Go back to the list of fields you asked the API for in Part 1. Which one do you think holds just the artist’s name, with nothing extra?

I changed it to artist title, but how do I prevent the function from printing null for unknown artist names instead of "Unknown". I already tried having the , in the get function be "Unknown"

Diagnosing why a missing-key check misses null values.

Good change. Now let’s look at the hint the checker gave you earlier:

Hint: .get(key, default) only uses the default when the key is missing, not when it's null.

Here’s what that means. For that Baroque Pearl artwork, the API does send an artist_title key, but its value is null, which Python turns into None. Since the key exists, .get thinks “found it!” and hands you None. Your "Unknown" default never gets used, because it’s only a backup for a missing key.

So you need a second check after the .get: “if what I got back is None, swap in "Unknown".” Here’s a tiny example with a different task:

python
nickname = user.get("nickname")
if nickname is None:
    nickname = "Friend"

Try predicting before you change your code: if user were {"nickname": None}, what would nickname hold after line 1, and what would it hold after line 3?

Stage 3:
I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: [name]([inputs]) takes [what] and returns [what].
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

I like this routine, and I’m ready to follow it. It looks like the template placeholders didn’t get filled in, though, so I don’t know what function to write yet.

Could you send me these three things?

Your attempt so far. Paste your code or describe your plan, even if it’s broken or half-finished.
Where you’re stuck, in one sentence.
The function you need: its name, its inputs, what it takes, and what it returns. For example: count_votes(responses) takes a list of survey answers and returns a dictionary of how many times each answer appeared.

It also helps to know which libraries you’re already using (for example, just plain Python, or something like Tkinter or Streamlit for the interactive part). That way I stay within what you know.

Once I have those, I’ll write the one function and then ask you to predict what it returns for a real input.

def save_results(artworks, filename):
    results = {}
    for art in artworks:
    txt.print(art.get("title", "Unknown"), art.get("artist_title", "Unknown"), art.get("date_display", "Unknown"))
    return results

this is my general idea. i dont know how to save the results or how to print it to a text file.

Figuring out the expected behavior of a results-saving function.

I filled in one detail you hadn’t decided: since the main job is writing to a file, I made it return how many artworks it saved. Tell me if you wanted it to return something else.

Two new things it uses:

open(filename, "w"): opens (or creates) a text file for writing, wiping anything already in it.
with ... as file:: keeps the file open for the indented block, then closes it automatically.
python
# AI-written
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

Predict before you run. Suppose you call it like this:

python
artworks = [
    {"title": "The Bedroom", "artist_title": "Vincent van Gogh", "date_display": "1889"},
    {"title": "Nighthawks", "date_display": "1942"},
]
save_results(artworks, "art.txt")
What will the function return?
What will be inside art.txt, line by line?

Write down your prediction first, then run it and tell me what you actually got.

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

I think the file will contain the results of all of the sample data's titles, artist's names, and dates printed on its own separate line for each item in the sample data.


Lion (One of a Pair, South Pedestal) | Edward Kemeys | 1893
Baroque Pearl Mounted as a Cat Holding a Mouse | None | 17th century
Nude with Cats | Pablo Picasso | 1901
Cat Making Up | Inagaki Tomoo | 1962
Homesickness | René Magritte | c. 1948
Winter: Cat on a Cushion | Théophile-Alexandre Pierre Steinlen | 1909
Border Fragments | Nasca | 100 BCE–200 CE
The Return of Odysseus (Homage to Pinturicchio and Benin) | Romare Howard Bearden | 1977
Lions on the Dreyfus Fund III | Larry Rivers | 1964
Summer: Cat on a Balustrade | Théophile-Alexandre Pierre Steinlen | 1909


## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I was wrong in that having a fallback doesn't gurantee "Unknown" being printed and had to make another check for it was null.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
I changed the filename to be based on the search term because just having something like "results.txt" can be pretty vague if you end up saving a lot of text files. Making the file name more search specific makes it easier to remember what file contains what from the name.