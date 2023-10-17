# map(function,data(list))

from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['tabish','shaikh','python']
anagrams = [ ]

for word in words:
    anagrams.append(jumble(word))
print(anagrams)

# using map function
print(list(map(jumble, words)))

# using comprehension
print([ jumble(word) for word in words ]) 