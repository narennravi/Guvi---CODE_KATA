# Question:-
'''
Given a string S convert each characters of the string into ASCII values and print the sum of the numbers.
Input Size : |s| <= 100000


Sample Testcase :
INPUT:
guvi

OUTPUT:
443
'''


# Solution;-
s=input()
sum=0
for i in range(len(s)):
  res=ord(s[i])
  sum=sum+res
print(sum)
