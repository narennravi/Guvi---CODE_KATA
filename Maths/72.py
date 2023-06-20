# Question:-
'''
Given a number N in decimal convert it into binary value.
Input Size : N <= 100000

Sample Testcase :
INPUT
5 

OUTPUT
101
'''


# Solution:-
n=int(input())
print(bin(n)[2::])
