# Question:-
'''
Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.

Sample Testcase :
INPUT
3
2 6

OUTPUT
yes
'''



# Solution:-
N = int(input())
L,R = map(int,input().split())

if N in range(L,R):
    print("yes")
else:
    print("no")
