# Question:-
'''
Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
Input Size : A,B,C <= 100000

Sample Testcase :
INPUT
3 4 5

OUTPUT
yes
'''


# Solution:-
A,B,C=(int(no) for no in input().split())
if(A!=B!=C):
  print('yes')
else:
  print('no')
