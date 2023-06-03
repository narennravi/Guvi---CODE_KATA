# Question:-
'''
Given a number N and an array of N integers, find the sum of all the negative numbers in the array.
Input Size : N <= 100000

Sample Testcase :
INPUT
2
3 0

OUTPUT
0
'''


# Solution:-
n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
sum = 0
for i in l:
    if i < 0:
        sum += i
print(sum)
