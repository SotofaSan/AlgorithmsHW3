

number = int(input('Enter a number: '))


def rec_factorial(n):
    if n > 1:
        return rec_factorial(n - 1) * n
    elif n == 1:
        return n
    else:
        print('wrong number')


print(rec_factorial(number))