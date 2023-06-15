# Question:-
'''
You are an intern at GUVI and the company wants to organise its data and delete unnecessary extra storage elements used.
You are given k arrays of unequal dimensions. Sort the k arrays individually and concatenate them.

Input Description:
First line contains the number of arrays. Subsequent lines contain the size of the array followed by the elements of the array.

Output Description:
An array containing the sorted elements of k sorted arrays

Sample Input :
3
2
98 12
6
1 2 3 8 5 9
1
11

Sample Output :
12 98 1 2 3 5 8 9 11
'''


# Solution:-
n = int(input())
a=[]
for i in range(n):
    s = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    a.extend(l)
print(*a)
