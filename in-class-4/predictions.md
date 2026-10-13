# Class 4: Five broken snippets

Your name: 
Collaborator: 

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

The print line will break. The error that will show is that there is "Room" in exhibit. It is 'room'. The fix is to make it lower case.
## Snippet 2
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?
The print line will break. The error is that you can't add an integer with a string. The fix is that you make the integer a string.

## Snippet 3
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

The line that breaks is the loop. It will be a bounds error because the i + 1 will go out of bounds. The fix is to get rid of the len + 1.
## Snippet 4
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?
The error is the print. The error is that you're printing visit instead of visits. The fix is to make it visits.

## Snippet 5
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

The line that breaks is the print(longest). The error is that it should be return. So that's the fix.
# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
- What error did Python show?
- What's the fix?

print("Find it in room " + exhibit["room"])
The error was a KeyError. I fixed it by making it lowercase.
## Snippet 2
- Which line broke?
- What error did Python show?
- What's the fix?

print("Find it in room " + exhibit["room"])
The error is TypeError and the fix is make it a , instead of a plus.
## Snippet 3
- Which line broke?
- What error did Python show?
- What's the fix?

print(i + 1, exhibits[i])
The error is IndexError.
It goes out of bounds so you need to make it enumerate.
## Snippet 4
- Which line broke?
- What error did Python show?
- What's the fix?

print(count_visits(visit, 243))
The error is a NameError. The fix is to make it visits. 
## Snippet 5
- Which line broke?
- What error did Python show?
- What's the fix?

print(title.upper())
The error is AttributeError. The fix is to make it Upper.
When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: N/A kinda confused what the chat is
- Our guess before asking: Done by myself because sick
- Chat: N/A
- Did it give you too much? What did you do?
N/A