# Question:-
'''
Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.

Input Description:
A single line containing an integer,n.

Output Description:
Print the smallest perfect power of 2 greater than n.

Sample Input :
48
Sample Output :
64
'''



# Solution:-
n=int(input())
N=1
while n>0:
  N=N<<1
  n=n>>1
print(N)