# Question:-
'''
Write a program to print the sum of the first K natural numbers.
Input Size : n <= 100000

Sample Testcase :
INPUT
3

OUTPUT
6
'''


# Solution:-
a = int(input())
sum = 0
for i in range(a+1):
    sum += i
print(sum)
