# Question:-
'''
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.

Sample Testcase :
INPUT
4 2
1 2 3 3

OUTPUT
yes
'''


# Solution:-
a,b = map(int,input().split())
arr = list(map(int,input().split()))

if b in arr:
    print("yes")
else:
    print("no")
