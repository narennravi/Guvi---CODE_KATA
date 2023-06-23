# Question:-
'''
Given a number N, print the sum of the squares of its digits.
Input Size : 1 <= N <= 1000000000000000000


Sample Testcase :
INPUT
19

OUTPUT
82

'''


# Solution:-
num = int(input())

def sum_of_squares_of_digits(num):
    return sum(map(lambda x: int(x) ** 2, str(num)))

print(sum_of_squares_of_digits(num))
