# Question:-
'''
Given 2 numbers N,M. Find their difference and check whether it is even or odd.

Sample Testcase :
INPUT
5 5

OUTPUT
even
'''


# Solution:-
N,M=(int(no) for no in input().split())
result=(N-M)%2
if result==0:
  print('even')
else:
  print('odd')
