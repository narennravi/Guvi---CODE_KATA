# Question:-
'''
Write a code to get an integer N and print the digits of the integer.

Input Description:
A single line contains an integer N.

Output Description:
Print the digits of the integer in a single line separated by space,

Sample Input :
348

Sample Output :
3 4 8
'''



# Solution:-
n = input()
l = [x for x in n]
num =' '.join(l)
print(num)
