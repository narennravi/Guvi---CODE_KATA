# Question:-
'''
Using the method of looping, write a program to print the table of 9 till N in the format as follows:
(N is input by the user)

9 18 27...

Print NULL if 0 is input

Input Description:
A positive integer is provided as an input.

Output Description:
Print the table of nine with single space between the elements till the number that is input.

Sample Input :
3
Sample Output :
9 18 27
'''



# Solution:-
a=int(input())
e=[]
for i in range(1,a+1):
    b=i*9
    e.append(b)
print(*e)