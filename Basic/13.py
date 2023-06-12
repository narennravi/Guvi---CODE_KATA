# Question:-
'''
Write a code to get an integer N and print the sum of  values from 1 to N.

Input Description:
A single line contains an integer N.

Output Description:
Print the sum of values from 1 to N.

Sample Input :
10

Sample Output :
55
'''



# Solution:-
num = int(input())
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while num > 0:
       sum =sum + num
       num =num - 1
   print(sum)
