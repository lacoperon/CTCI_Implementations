'''
Elliot Williams
08/02/18

Q: `Palindrome Permutation`: Given a string, write a function to check if it is
   a permutation of a palindrome.
'''

def isPalinPermute(input):
    # Defines set of all letters with only one instance in the string
    letterSet = set()
    for letter in input.lower():
        if letter is not " ":
            if letter not in letterSet:
                letterSet.add(letter)
            else:
                letterSet.remove(letter)

    # A palindrome necessarily has only one, or exactly zero, of these letters
    return len(letterSet) in [0,1]

assert isPalinPermute("Taco Cat")
assert isPalinPermute("A man a plan a canal Panama")
assert isPalinPermute("")

assert not isPalinPermute("aaabbbccc")
assert not isPalinPermute("Some nights I stay up, cashing in my bad luck")
