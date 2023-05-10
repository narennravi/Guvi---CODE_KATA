# Question:-
'''
You are given an array of ‘N’ numbers.You have to find the sum of XOR pairs of numbers in the array.

Input Description:
The first line of input denotes a number n. Next line contains n space separated numbers

Output Description:
Print the sum of all XOR pairs present in array

Sample Input :
3
7 3 5
Sample Output :
12
'''



# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
sm = 0

for i in range(n):
    for j in range(i+1, n):
        sm += (l[i] ^ l[j])
print(sm)