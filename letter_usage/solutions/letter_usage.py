"""
You are given a phrase.

You need to return a dictionary containing the number of time each letter appears in the phrase.

"My name is Fred"
answer = {
    "M": 1,
    "y": 1,
    " ": 3,
    "n": 1,
    "a": 1,
    "m": 1,
    "e": 2,
    "i": 1,
    "s": 1,
    "F": 1,
    "r": 1,
    "d": 1}
"""

def char_count(phrase):
    answer = {}
    for c in phrase:
        if c not in answer:
            answer[c] = 1
        else:
            answer[c] += 1
    return answer

print(char_count("My name is Fred"))