# Write a function for decompressing string “a4b3c2d” => "aaaabbbccd"

string1 = input(f"Enter a string: ")

def str_decompress(string):
    result = ''

    for i in range(0, len(string)):
        if string[i].isnumeric():
            result += ''
        else:
            if i != len(string) - 1:

                if string[i + 1].isnumeric():
                    result += string[i] * int(string[i + 1])
                else:
                    result += string[i]
            else:
                result += string[i]

    return result

print(str_decompress(string1))