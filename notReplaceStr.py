# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings.
# DON’T USE METHOD REPLACE

string1 = input(f"Enter a string: ")
string2 = input(f"Enter a first substring: ")
string3 = input(f"Enter a second substring: ")

def notReplace(string, sub1, sub2):

    return sub2.join(string.split(sub1))

print(notReplace(string1, string2, string3))

# substring should not be doublicated?