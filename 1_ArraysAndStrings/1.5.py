'''
Elliot Williams
08/02/18

Q: `One Away`: There are three types of edits that can be performed on strings:
   insert a character, remove a character, or replace a character. Given two
   strings, write a function to check if they are one edit (or zero edits) away.
'''

def isOneAway(input1, input2):

    lengthDiff = len(input1) - len(input2)
    if abs(lengthDiff) > 1:
        return False # Must be almost the same length to be 'one away'

    # Now, we iterate over both strings, allowing for one (and only one) mistake
    changeMade = False
    j = 0
    for i in range(len(input1)):
        # If j is too long, then we can use it as our one mistake
        if j == len(input2):
            return not changeMade # True if no mistake made before, else False

        letter1 = input1[i]
        letter2 = input2[j]

        # If this is true, a mistake has been seen
        if letter1 != letter2:
            # Must not have made a prior mistake
            if not changeMade:
                if abs(lengthDiff) is 1:
                    # Moves j 'back' if input1 has insertion relative to input2,
                    # and 'forward' if there is a deletion
                    j -= lengthDiff

                    # If there's been a deletion, make an extra comparison
                    if lengthDiff == -1:
                        if letter1 != input2[j]:
                            return False
                changeMade = True
            else:
                return False # If we'e already made a mistake, not 'one away'

        j += 1
    return True

# Time  Complexity: O(N)
# Space Complexity: O(1)

assert isOneAway("pale", "ple")
assert isOneAway("pales", "pale")
assert isOneAway("pale", "bale")
assert not isOneAway("pale", "bake")
