# Question:-
'''
Given a sentence S take out the extra spaces.If no extra space is present print the same as output.
Input Size : |s| <= 100000(complexity O(n))

Sample Testcase :-
INPUT:
codekata challenge

OUTPUT:
codekata challenge
'''



# Solution:-
S=input()
res=" ".join(S.strip().split())
print(res)
