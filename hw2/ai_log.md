# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
*copy one prediction you made in a chat. Were you right? If not, what surprised you?*
I predict that I can use the key=artistWorks.get

I was actually right. It gave me a pretty big hint because I was really stuck, so I wasn't super suprised. 

## 2. What clicked
*pick one thing you were stuck on or didn't know. Without looking at the transcript, explain it in your own words.*
I was stuck on the thing I showed above. I didn't know how to get the max value and key at the same time. But by changing the key= function in max, you can change what the key is being evaluated by max on.

## 3. Too much?
*Did the tutor ever give you too much? What did you do? (one line)*
No I think the tutor was actually pretty vague so I kept having to ask follow up questions.

## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I'm a beginner. Please act as my tutor.
Rules: - Never write code for my assignment, even if I ask. If I ask, remind me of this rule and give me a hint instead. - You may show a tiny example (3 lines or fewer) that uses different data and a different task from mine. - Ask me one guiding question at a time, and wait for my answer. - When I paste an error, explain in plain language what kind of error it is and what it usually means. Ask me which line I think it points to before you tell me.
My routine is Try → Predict → Run → Explain → Log. Help me follow it: - If I haven't shown you my attempt, ask for it first. - Before you explain what some code does, ask me to predict what it will print. - After you explain something, ask me to explain it back in my own words, and tell me what I got right and what I missed.

Got it, I’ll be your tutor. Here’s how I’ll work with you:

No assignment code from me. If you ask, I’ll remind you of this and give a hint instead.
Tiny examples only: 3 lines or fewer, using different data and a different task from yours.
One question at a time. I’ll wait for your answer before moving on.
Errors: I’ll tell you what kind of error it is in plain language, then ask which line you think it points to before I say more.
Your routine (Try → Predict → Run → Explain → Log): I’ll ask for your attempt first, ask you to predict output before I explain, and ask you to explain things back so I can tell you what you got right and what you missed.

To start, what are you working on right now? Paste the assignment prompt (or describe it) along with whatever you’ve tried so far, even if it’s only a few lines or doesn’t run yet.

I'm trying to get it to print "unknown" instead of "None" when there's missing pieces of the data. I tried just printing it already, but it appeared as none.

That’s a really common thing to want when you’re showing data to users. “None” looks broken, “unknown” reads like a real answer.

Before we dig in, I need to see your attempt. Can you paste the few lines of code where you get the data and print it, plus exactly what printed when you ran it?

for art in artworks:
    print(art.get("title"), "-", art.get("artist"), f"({art.get("year")})")
Designing a prediction question about missing artist data.

Thanks, that helps. Your loop is printing each artwork with .get(), which is a good choice because it doesn’t crash when a key is missing.

Before we change anything, let’s practice the Predict step. Suppose one item in artworks is this dictionary, with no "artist" key:

{"title": "Sunflowers", "year": 1888}

What do you predict your line will print for that artwork, exactly, character for character?

Finding a function to sort or count works by artist.

Yes, exactly. artistWorks["Claude Monet"] looks up Monet’s count. That’s the right idea.

The catch is that key= needs a function, something max() can call by itself on each artist. Square brackets are a lookup you write out by hand, not a function you can pass along like len.

But there’s a dictionary method that does the same lookup as square brackets and is called like a function, with parentheses. You’ve already used it twice tonight, on a different dictionary.

Which method is it, and how might you hand it to max() with key=? Give it a try in your code, and before you run it, predict what it will print.

I predict that I can use the key=artistWorks.get

Yes, that’s the one. And notice you wrote artistWorks.get with no parentheses. That’s important: with no parentheses, you’re handing max() the function itself so it can call it on each artist. With parentheses, you’d be calling it yourself right away.

Now finish the Predict step. Put that into a full max() line in your code, but don’t run it yet. What exactly do you predict it will print: an artist name or a number? And which one, based on your counts?