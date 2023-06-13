# Question:-
'''
Given a string S consisting of 2 words reverse the order of two words .
Input Size : |S| <= 10000000

Sample Testcase :
INPUT
hello world

OUTPUT
world hello
'''


# Solution:-
n = list(map(str,input().split()))
n.reverse()
print(*n)
