# Question:-
'''
Given a string S, print the reverse of the string after removing the vowels.If the resulting string is empty print '-1'.
Input Size : 1 <= N <= 100000

Sample Testcase :-
INPUT:
codekata

OUTPUT:
tkdc
'''


# Solution:-

S=input()
ls=""
for i in S:
    if i not in "aeiouAEIOU":
        ls=ls+i
if ls=="":
    print("-1")
else:
    print(ls[::-1])

