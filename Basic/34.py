# Question:-
'''
Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))

Sample Testcase :
INPUT
codekata

OUTPUT
ocedakat
'''


# Solution:-
S=input()
t=list(S)
t[::2],t[1::2]=t[1::2],t[::2]
res=''.join(t)
print(res)
