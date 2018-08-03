'''
Elliot Williams
08/02/18

Q: `Check Permutation`: Given two strings, write a method to decide if one is a
   permutation of the other.
'''

def isPermute(input1, input2):

    # Helper function to count / alter a frequency dictionary of letters
    def countLetters(input, countStep, letterDict={}):
        for letter in input:
            # Assigns the frequency of a letter to be the previous frequency
            # plus one if previously present in letterDict, otherwise 1
            letterDict[letter] = letterDict.get(letter, 0) + countStep
        return letterDict

    if len(input1) is not len(input2):
        return False

    # Creates dict of letters in input1 with their frequencies
    letterDict = countLetters(input1, 1)
    # Creates dict of letters w the difference in freqs bw input1 and input2
    letterDictDec = countLetters(input2, -1) #

    # letterDictDec will be `None` if any letter has negative frequency in
    # the second call to `countLetters`, short circuiting the computation
    # to prevent unnecessary work
    if not letterDictDec:
        return False

    # All frequency values should be 0 in the `letterDictDec` if input2 is
    # a permutation of input1
    for value in letterDictDec.values():
        if value is not 0:
            return False
    return True

# Time  Complexity: O(N + K) ~= O(N)
# Space Complexity: O(K)


assert isPermute("waterbottle", "bottlewater")
assert isPermute("", "")
assert isPermute("a", "a")

assert not isPermute("waterbottle", "sodabottle")
assert not isPermute("waterbottle", "")
assert not isPermute("", "sodabottle")
