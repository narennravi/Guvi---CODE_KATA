# Question:-
'''
Given a binary number convert it into octal format.

Sample Testcase :-
INPUT:
1100100

OUTPUT:
144
'''


# Solution:-
a=int(input(),2)

res=oct(a)
print(res[2::])
