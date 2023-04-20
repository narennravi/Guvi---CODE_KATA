# Question:-
'''
Generate a hollow inverted half pyramid pattern using numbers.


Input Description:
Given an integer R indicates number of rows.

Where 1<=R<=100.


Output Description:
Print the hollow Inverted half pyramid pattern using numbers based on the given integer R.

Sample Input :
5
Sample Output :
12345
1  4
1 3
12
1
'''




# Solution:-
n = int(input())
for i in range(n):
  p=1
  for j in range(i,n):
    if(i==0 or j==i or j==n-1):
      print(p, end="")
    else:
      print("", end=" ")
    p+=1

  print()
