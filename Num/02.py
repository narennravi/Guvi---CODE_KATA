# Question:-
'''
You are given an array of digits. Your task is to print the digit with maximum frequency.

Input Description:
You are given length of array ’n’,next line contains n space separated numbers.

Output Description:
Print the number with maximum frequency. If two number have equal freqency prin the number that comes first

Sample Input :
7
1 2 3 4 4 4 5
Sample Output :
4
'''


# Solution;-
n = int(input())
l = input().split(" ")
freq = l[0]
count = 0
for i in range(n):
    curr_freq = l.count(l[i])
    if curr_freq > count:
        count = curr_freq
        freq = l[i]
print(freq)