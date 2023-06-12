# Question:-
'''
Given numbers A,B find A^B.
Input Size : 1 <= A <= 5 <= B <= 50

Sample Testcase :
INPUT
3 4

OUTPUT
81
'''



# Solution:-
import math
A,B=(int(no) for no in input().split())
result=math.pow(A,B)
print(round(result))
