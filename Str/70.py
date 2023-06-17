# Question:-
'''
Given a string S, print 'yes' if the strings 'GUVI' and 'GEEK' is present case-sensitively in the string else print 'no'.
Input Size : 1 <= 100


Sample Testcase :
INPUT:
Vishal_Sundar prepared this question

OUTPUT:
no
'''

# Solution:-
s=input().split()
sample=['GUVIGEEK']
#sample1=['GEEK']

l=[]
for i in range(len(s)):
  if s[i] in sample:
    #f s[i] in sample1:
      l.append(s[i])

if len(l)>0:
  print("yes")
else:
  print("no")
