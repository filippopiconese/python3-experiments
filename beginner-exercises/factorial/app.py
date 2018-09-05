'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


number = int(input('Insert a number: '))

print(f'{factorial(number)}')
