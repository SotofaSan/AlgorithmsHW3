# Write a Python function, which will count
# how many times a character (substring) is included in a string.
# DON’T USE METHOD COUNT

string1 = input(f"Enter a string: ")
string2 = input(f"Enter a substring: ")

def notCount(string, substring):
    count = 0
    lensub = len(substring)

    for i in range(lensub, len(string) + 1):
        if string[i - lensub:i] == substring:
            count += 1
    return count


print(notCount(string1, string2))