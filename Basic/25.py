# Question:-
'''
Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124

Sample Output :
7
'''


# Solution:-
n = int(input())
total = 0

while n > 0:
    dig = n % 10
    total = total + dig
    n = n // 10
print(total)
