# Question:-
'''
Given a number N, print 'yes' if it is composite else print 'no'.

Sample Testcase :
INPUT
123

OUTPUT
yes
'''

# Solution:-
N=int(input())
count=0
for i in range(2,N):
  if N%i==0:
      count=count+1
if count>=1:
  print('yes')
else:
  print('no')
