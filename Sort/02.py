# Question:-
'''
You are given a number ‘n’. Your task is to create the smallest number possible using the digits of number. The number should be of the same length as the orignal input number.

Input Description:
You are given a number ‘n’,

Output Description:
Print the smallest possible number of same length

Sample Input :
123456789123456789
Sample Output :
112233445566778899
'''


# Solution:-
n = list(input())
c = n.count("0")
n.sort()
s = n[c] + "0"*c
for i in range(c+1, len(n)):
    s += n[i]
print(int(s))
