# Question:-
'''
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
'''



# Solution:-
N,K = (int(no) for no in input().split())
ele=list(map(int, input().split()))
res=ele.count(K)

if res>1:
  print(res)
elif res==1:
  print("0")
else:
  print("-1")