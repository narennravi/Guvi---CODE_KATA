# Question:-
'''
Given a string S, print the encoded string by adding 3 to each character(a maps to d,b maps to e,c maps to f and so on).
Input Size : 1 <= N <= 100000

Sample Testcase :
INPUT
RADAR

OUTPUT
UDGDU
'''


# Solution:-
s=input()
ls=[]
for i in range(len(s)):
  if (ord(s[i])== 88): 
    ls.append(chr(65))
  elif (ord(s[i])==120):
    ls.append(chr(97))
  elif (ord(s[i])==89):
    ls.append(chr(66))
  elif (ord(s[i])==121):
    ls.append(chr(98))
  elif (ord(s[i])==90):
    ls.append(chr(67))
  elif (ord(s[i])==122):
    ls.append(chr(99))
  else:
    res=ord(s[i])
    sum=res+3
    opt=chr(sum)
    ls.append(opt)
print(*ls,sep="")
