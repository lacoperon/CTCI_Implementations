'''
Elliot Williams
08/02/18

Q: `String Compression`: Implement a method to perform basic string compression
   using the counts of repeated characters. For example, the string
   `aabcccccaaa` -> `a2b1c5a3`. Your method should return the smaller of the
   compressed and uncompressed strings.
'''

def compressString(input):
    comp_str = ""
    currentLetter = None
    letterFreq = 0
    for letter in input:
        if letter != currentLetter:
            if currentLetter:
                # The letter has changed; add currentLetter + count to comp_str
                comp_str += "{}{}".format(currentLetter, letterFreq)
            currentLetter = letter
            letterFreq = 0
        letterFreq += 1
    # Finally, add the final currentLetter + count to comp_str
    comp_str += "{}{}".format(currentLetter, letterFreq)

    # Returns the shorter of [comp_str, input]
    if len(input) >= len(comp_str):
        return(comp_str)
    else:
        return(input)

assert compressString("aabcccccaaa") == "a2b1c5a3"
assert compressString("abcba") == "abcba"
