# Question:-
'''
You are given a number ‘n’,count the number of 1’s in its binary string.of that number

Input Description:
You are given with the number ‘n’.

Output Description:
Count the number of 1 in string

Sample Input :
4
Sample Output :
1
'''



# Solution:-
n = int(input())
a = (str(bin(n))[2:]).count('1')
print(a)