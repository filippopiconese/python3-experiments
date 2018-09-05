'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

min = 2000
max = 3200
divisible = 7
multiple = 5

numbers = []

for number in range(min, max + 1):
    if number % divisible == 0 and number % multiple != 0:
        numbers.append(str(number))

print(','.join(numbers))
