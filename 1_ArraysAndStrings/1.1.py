'''
Elliot Williams
08/02/18

Q: `Is Unique`: Implement an algorithm to determine if a string has all
   unique characters. What if you cannot use additional data structures?
'''

# Attempt 1 : Using a set for an intuitive solution
def isUniqueChars(input):
    charSet = set()
    for char in input:
        if char in charSet:
            return False
        else:
            charSet.add(char)
    return True

# Time  Complexity: O(min(N,C))
# Space Complexity: O(K), in which K is the number of unique chars in input

# Attempt 2 : Implementation only using arrays
def isUniqueChars2(input):
    charList = []
    for char in input:
        if char in charList:
            return False
        else:
            charList.append(char)
    return True

# Time  Complexity: O(N*K)
# Space Complexity: O(K), in which K is the number of unique chars in input
# ... but this is silly, because computer do indeed have other data structures

# Tests:
assert isUniqueChars( "")
assert isUniqueChars2("")

assert isUniqueChars( "abcdefgh")
assert isUniqueChars2("abcdefgh")

assert isUniqueChars( "habdcewt")
assert isUniqueChars2("habdcewt")

assert not isUniqueChars("aa")
assert not isUniqueChars("aa")

assert not isUniqueChars("abab")
assert not isUniqueChars("abab")
