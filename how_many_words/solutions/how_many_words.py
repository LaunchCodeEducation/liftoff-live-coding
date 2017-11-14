'''
Given a phrase you need to return the number of words in the phrase.


"The dog jumps over the cat."
answer = 6
'''

def count_words(phrase):
    split_phrase = phrase.split(' ')
    return len(split_phrase)

def count_word(phrase):
    num_of_words = 1
    for c in phrase:
        if c == ' ':
            num_of_words += 1
    return num_of_words

print(count_words("The dog jumps over the cat."))
print(count_word("The dog jumps over the cat."))
print(count_words("cat"))
print(count_word("cat"))
