# Question:-
'''
Write a code to get the input in the given format and print the output in the given format.

Input Description:
A single line contains a string.

Output Description:
Print the characters in a string separated by comma.

Sample Input :
guvi
Sample Output :
g,u,v,i
'''


# Solution;-
name = input()

for i in name[:len(name)-1]:
    print(i, end=',')

print(name[len(name)-1])