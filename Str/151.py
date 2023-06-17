# Question:-
'''
Given a string S of length N, find whether the given string is a palindrome using stack or linked list and print 'yes' otherwise print 'no'.
Input Size : 1 <= N <= 100000


Sample Testcases :
INPUT:
GuviGeek

OUTPUT:
no
'''


# Solution:-
s=input()
ls=[]

#storing element one by ine
for i in s:
  adding_value=ls.append(i)

#print(ls)
lst_str=''.join(map(str,ls))

#print(lst_str)
#remove element one by one and store in another list
str_pop=''
i=0

while (i<len(s)):
  str_pop=str_pop+ls.pop()
  i=i+1
#print(str_pop)

#comparing 2 values
if (lst_str==str_pop):
  print("yes")
else:
  print("no")
