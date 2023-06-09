# Question:-
'''
Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd
'''



# Solution:-
n,m = input().split()
a = int(n)+int(m)
if a % 2 == 0:
    print("even")
else:
    print("odd")