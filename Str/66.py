# Question:-
'''
Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).


Sample Testcase :-
INPUT:
hello

OUTPUT:
he*lo
'''



# Solution:-

S=input()
mid=len(S)//2
if len(S)%2==0:
  print(S[0:mid-1]+"**"+S[mid+1:])
else:
  print(S[0:mid]+"*"+S[mid+1:])
