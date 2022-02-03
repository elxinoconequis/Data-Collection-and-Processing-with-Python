# ZIP lesson
# is python operation that takes 2 operations and zips them together, matching each of elements.
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)


# Consider a function called possible, which determines whether a word is still possible to play in
#  a game of hangman, given the guesses that have been made and the current state of the blanked word.

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# we can rewrite this using the zip function

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# # ---
# Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list,
#  L3, that sums the two numbers if the nfrom L1 is greater than 10 and the number from L2 is less than 5. 
#  This can be accomplished in one line of code.

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3=[(x1+x2)for (x1,x2) in zip(L1,L2) if (x1>10)and(x2 < 5)]
print(L3)