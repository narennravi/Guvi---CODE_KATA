# Question:-
'''
Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1

Sample Testcase :
INPUT
10 5

OUTPUT
5
'''



# Solution:-
import math
from fractions import gcd
N,M=(int(no) for no in input().split())
result= math.gcd(N,M)
if N!=0 and M!=0:
  print(result)
else:
  print("-1")
