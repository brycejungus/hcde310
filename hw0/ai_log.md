# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

```
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for students who want to search for relevant artwork with a keyword. My sketch is attached; follow it. Explain how the code works in plain language, section by section.
```

**AI's reply:**

Ran 3 commands, created a file, read a file
I built the app in art-search.html, 140 lines, laid out like your sketch. At the top is the title. Below it is a rounded search bar with a 🔍 button and a filter button (☰) beside it. Results show in a 3-column grid of cards. Each card has the image, a ★ in its top-right corner, and the title and artist underneath.
I tested it with fake API data: search, filters, stars and the favorites view all worked. I couldn't test it against the real Art Institute API, because my sandbox can't reach that website. To try it for real, open the file in your browser, search a word like "cat," then open ☰ and turn on each filter one at a time.
How the code works, section by section
The comments in the file are numbered to match these sections.
1. Styles (<style>). This controls how the page looks:
.search makes the pill-shaped search bar with the 🔍 button attached on the right, like your drawing.
.grid makes the 3-column card layout. The @media rules change it to 2 columns on narrow screens and 1 on phones.
.card-img gives every image box the same 4:3 shape. object-fit: cover crops images to fit, so the grid stays even.
.star puts the ★ in the top-right corner of the image, and .star.on turns it gold.
2. Page structure (HTML). These are the parts that are always on the page:
The title.
A <form> holding the search box and the ☰ button. Using a form means pressing Enter runs the search.
A filter panel that stays hidden until you click ☰. It has three options:
Type: Painting, Print, and so on.
Public domain only: artwork that's free to reuse, which is handy for student projects.
★ Favorites only: shows just the cards you've starred.
An empty status line and an empty grid. JavaScript fills these in later.
3. Setup. This stores the API address and FIELDS, the list of data we ask for: id, title, artist, date and image id. Asking only for what the cards show keeps responses small. $("x") is a shortcut for document.getElementById("x"). favorites is a Map, which works like a dictionary: it remembers starred artworks by their id. Favorites only last while the page is open. Refreshing clears them.
4. buildUrl(). This turns what you typed and chose into a web address for the API. URLSearchParams does the formatting, such as turning spaces into %20. Each filter you turn on adds one rule, like query[bool][filter][0][term][is_public_domain]=true. That long bracket format is how this API accepts filters in a URL. Roughly, it reads: "search, and keep only results where public domain is true."
5. search(). This is the main function. It runs when you search or change a filter:
If "Favorites only" is on, it skips the API and shows your starred cards.
If the search box is empty, it shows a hint instead.
Otherwise it calls fetch(...) to ask the API for results. await means "wait for the answer before moving on."
The API also returns the base address for images, called iiif_url, which gets saved for the next step.
try/catch catches failures, like no internet, and shows a friendly message instead of breaking the page.
6. render(). This draws the cards. It clears the grid, then builds one <article> card per artwork and adds it to the page. The API doesn't send image files directly. It sends an image_id, and the code builds the image address from it: .../iiif/2/{image_id}/full/843,/0/default.jpg. The 843, part means "843 pixels wide." loading="lazy" means images further down the page only load when you scroll to them.
7. Favorites. Clicking ★ runs toggleFavorite, which adds the artwork to favorites or removes it, then redraws the cards so the star changes color. safe() "escapes" text, meaning it converts characters like < into a harmless form. Without it, a title containing < could break the page's HTML.
8. Wiring up events. This connects actions to functions:
Submitting the form runs search(). e.preventDefault() stops the browser's default of reloading the page.
Clicking ☰ shows or hides the filter panel.
Changing any filter runs search() right away.


### Prompt 2

```
Can you add a feature that clears the search and brings it back to how it looks before you searched?
```

**AI's reply:**

Read 2 files, ran a command
I added a ✕ button inside the search bar, just left of 🔍. Clicking it, or pressing Esc while typing in the box, puts the page back to how it looked before you searched:
The search box empties and the cursor goes back into it.
The filters reset (Type goes back to "Any," both checkboxes turn off) and the filter panel closes.
The cards disappear and the "Type a keyword…" hint comes back.
Your ★ favorites stay saved, since you probably don't want one click to erase them. I tested the ✕ button, the Esc key and the favorites with fake data, and they all worked.
The file is now 164 lines, a bit over your ~150 target. If you need to cut it down, dropping the Esc shortcut and the 7b comment lines gets you close.
What changed in the code
Styles (section 1). Two new lines:
One styles the ✕ button in light gray.
One hides the browser's built-in ✕. Some browsers, like Chrome, show their own ✕ in search boxes, but it only clears the text, so you'd have two ✕s doing different things.
Page structure (section 2). There's a new <button id="clearBtn">✕</button> inside the search bar. It's type="button", not type="submit", so clicking it doesn't also run a search. The hint text was also moved out of the HTML into one variable called START_MESSAGE. That way the first page load and the clear button show exactly the same message.
Setup (section 3). searchCount is a new counter that fixes a subtle bug. Say you search "dog," then clear before the API answers. Without the counter, the dog results would pop onto your freshly cleared page a moment later. Now every search and every clear adds 1 to the counter. When an answer arrives, search() checks whether its number is still the latest, and if not, it throws the answer away.
7b. clearSearch(). This is the new function, and it runs one step for each thing on the page:
Increase searchCount, so any search still loading gets ignored.
Empty the search box.
Reset the Type dropdown and uncheck both checkboxes.
Close the filter panel.
Forget the last results and redraw the empty grid with the hint message.
Put the cursor back in the search box so you can type right away.
Wiring up events (section 8). Clicking ✕ now runs clearSearch. Pressing Esc in the box does the same. At the very end, render([], START_MESSAGE) draws the starting screen when the page first loads, using the same code the clear button uses.


(Copy the block above for more prompts.)


### Prompt 3

```
can you add a home page that has messages like "ready for your search", "awaiting your search", and fun ones like "well I'm not gonna search the art myself..". When a user clicks the x in the search bar it should bring them back to this page
```

**AI's reply:**

(paste the reply)
Ran 2 commands, read a file
The app now has a home page. It's what you see when the page first loads, and clicking ✕ (or pressing Esc) brings you back to it. The search bar stays at the top, so you can search right from home. I tested this with fake data: the page opens on home, a search swaps home for the cards, and ✕ brings home back with a new message.
Each time the home page appears, it shows one random message in large text:
"Ready for your search."
"Awaiting your search…"
"Well, I'm not gonna search the art myself…"
"The paintings are getting restless."
"300,000 artworks, zero searches. Your move."
"Go on, type something. The Monets won't bite."
The last three are extras I added in the same spirit as yours; edit or delete them freely. The same message never shows twice in a row. Pressing Enter with an empty search box also brings you back to home.
The file is now 196 lines, well past your ~150 target. The home page is about 30 of those lines. If you need to trim, cutting some messages or the Esc shortcut helps a little.
What changed in the code
Styles. The new .home rules center the message and make it big and bold, with a smaller gray hint line under it. The [hidden] rule makes sure anything marked hidden really disappears. Without it, the grid's own display: grid style could keep it visible.
Page structure. There's a new <section id="home"> with two lines:
homeMsg, which starts empty. JavaScript puts the random message there.
The hint: "Type a keyword above and press Enter…"
The status line and card grid now start with hidden, since home is what shows first.
Setup. HOME_MESSAGES is the list of messages. It's an array, which is an ordered list, so adding a message just means adding another line in quotes followed by a comma. lastMessage remembers which one was just shown.
7c. showHome(). This is the new function:
Math.random() gives a random number from 0 up to (but not including) 1. Multiplying it by the number of messages and rounding down with Math.floor picks a random position in the list.
The do … while loop means "pick one, and pick again if it's the same as last time."
It shows the home section and hides the status line and grid.
render(). Its first two lines now do the opposite of showHome(): hide home, show the status line and grid. So any search result automatically leaves the home page.
Replacing the old start message. Everywhere the code used to show "Type a keyword and press Enter," it now calls showHome(). That happens in three places: when the page first loads, when you search with an empty box, and at the end of clearSearch().

(Copy the block above for more prompts.)
