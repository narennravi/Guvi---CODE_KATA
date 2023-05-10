# Question:-
'''
You are given a number ‘n’ and a bit ‘K’,your task is to tell whether the first bit is 1. Return true or false according to the scenario. First bit starts from right.(0 based indexing)

Input Description:
You are given a number ‘n’ and a bit ‘k’.

Output Description:
Print true if bit is set and false if bit is not true.

Sample Input :
4
0
Sample Output :
False
'''



# Solution:-
n = int(input())
bit = int(input())
a = list(str(bin(n))[2:])
a.reverse()
if a[bit] == '1': print('true')
else: print('False')