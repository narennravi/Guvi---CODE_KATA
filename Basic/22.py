# Question:-
'''
Given an array of N elements switch(swap) the element with the adjacent element and print the output.

Sample Testcase :
INPUT
5
3 2 1 2 3

OUTPUT
2 3 2 1 3
'''


# Solution:-
n = int(input())
a = list(map(int,input().split()))

for i in range(0,len(a)-1,2):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
print(*a)
