# Question:-
'''
You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1
Sample Output :
1
'''




# Solution:-
x,y = map(int,input().split())
if x<y:
    print(x)
else:
    print(y)