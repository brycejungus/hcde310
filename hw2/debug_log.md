# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
  File "/Users/brycejung/HCDE/HCDE 310/hcde310/hw2/part2.py", line 9, in <module>
    print(art["title"], art["artist"])
                        ~~~^^^^^^^^^^
KeyError: 'artist'

### 2. What I thought it meant
I thought it meant that artist didn't exist in the dictionary for every entry.

### 3. What it actually meant
It means it doesn't exist for specific entries in the dictionary, not all.

### 4. The fix
By using .get, you can avoid this.

## Entry 2

### 1. Error message
*copy it exactly*
  File "/Users/brycejung/HCDE/HCDE 310/hcde310/hw2/part3.py", line 17
    artistWorks[artist]++
                         ^
SyntaxError: invalid syntax

### 2. What I thought it meant
I thought it means that there's something wrong with the syntax.

### 3. What it actually meant
It means you can't do that in python. While that's something you can do in Java, you can't in python.

### 4. The fix
Instead of doing ++, you do += 1