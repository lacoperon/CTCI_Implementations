'''
Elliot Williams
08/02/18

Q: `URLify`: Write a method to replace all spaces in a string with '%20'. You
   may assume that the string has sufficient space at the end to hold the
   additional characters, and that you are given the "true" length of the string
'''

def URLify(char_array, true_length):
    j = len(char_array) - 1 # index of last character

    # Iterates through characters in char_array in reverse,
    # to prevent overwriting necessary characters
    for i in reversed(range(len(char_array))):
        current_char = char_array[i]
        if current_char is not None:
            if current_char is " ":
                # Adds in %20 in appropriate places, and goes back 3 characters
                char_array[j] = "0"
                char_array[j-1] = "2"
                char_array[j-2] = "%"
                j -= 3
            else:
                char_array[j] = current_char
                j -= 1
    return char_array

# Time  Complexity: O(N)
# Space Complexity: O(1) ~in place~

# Helper function to generate appropriate input
def char_arrayify(input):
    num_spaces = 0
    char_array = []
    for char in input:
        if char is " ":
            num_spaces += 1
        char_array.append(char)

    char_array += [None] * num_spaces * 2
    return char_array

fox_str = "The Fox jumped quickly"
empty_str = ""
borg_str  = "NoSpacesAreNecessaryForTheBorg"

fox_example   = (char_arrayify(fox_str), len(fox_str))
empty_example = (char_arrayify(empty_str), len(empty_str))
borg_example  = (char_arrayify(borg_str), len(borg_str))

print("".join(URLify(*fox_example)))
print("".join(URLify(*empty_example)))
print("".join(URLify(*borg_example)))
