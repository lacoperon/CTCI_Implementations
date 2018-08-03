'''
Elliot Williams
08/02/18

Q: `String Rotation`: Assume you have a method isSubstring which checks if one
   word is a substring of another. Given two strings, s1 and s2, write code to
   check if s2 is a rotation of s1 using only one call to isSubstring
   (e.g. "waterbottle" is a rotation of "erbottlewat")
'''

def isRotation(s1, s2):
     # Assumedly you wouldn't want to call this on two strings w diff len
    if len(s1) is not len(s2):
        return False

    # Define ds2 to be two copies of s2 concatenated together
    ds2 = s2 * 2

    # By def of rotation, ds2 must contain s1 if s1 is a rotation of s2
    return s1 in ds2

# Time  Complexity: O(N) (Assuming optimal substring method in Python)
# Space Complexity: O(N)

assert isRotation("erbottlewat", "waterbottle")
assert isRotation("","")
assert isRotation("a","a")

assert not isRotation("a","b")
assert not isRotation("abc","ab")
assert not isRotation("hello","panda")
