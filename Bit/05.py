# Question:-
'''
Given a number N and an array of N integers, find the maximum of Bitwise OR of all segments.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6
'''



# Solution:-
n = int(input())
l = input().split(" ")
bit = int(l[0])

for i in l:
  bit = bit | int(i)
print(bit)