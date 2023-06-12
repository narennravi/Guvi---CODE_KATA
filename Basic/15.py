# Question:-
'''
Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
Input Size N <= 100000

Sample Testcase :
INPUT
4
4 3 2 1

OUTPUT
0
'''



# Solution:-
N = int(input())
arr = list(map(int, input().split()))

result = arr[0]
for i in range(1, N):
    result &= arr[i]

print(result)
