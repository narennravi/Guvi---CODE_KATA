# Question:-
'''
Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -1
Input Size : |sentence| <= 1000000(complexity O(n)).

Sample Testcase :
INPUT
I enjoy doing codekata
codekata

OUTPUT
1
'''


# Solution:-
S=input().split()
K=input()
res=S.count(K)
if (res>=1):
  print(res)
else:
  print("-1")
