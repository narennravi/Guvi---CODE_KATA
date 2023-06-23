# Question:-
'''
Given 3 numbers A,B,C find (A^B)%C.
Input Size : A,B,C <= 1000000000


Sample Testcase :
INPUT
3 4 1000000007

OUTPUT
81
'''


# Solution:-
a,b,c=(int(no) for no in input().split())
print((a**b)%c)
