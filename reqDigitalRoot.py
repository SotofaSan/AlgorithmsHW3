
number = int(input('Enter a number: '))


def req_sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10 + req_sum_of_digits(int(n / 10)))

def req_digital_root(n):
    if req_sum_of_digits(n) > 9:
        print(req_sum_of_digits(n))
        return req_sum_of_digits(req_sum_of_digits(n))
    else:
        return req_sum_of_digits(n)


print(req_digital_root(number))