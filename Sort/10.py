# Question:-
'''
Bubble sort is based on the idea of repeatedly comparing pairs of adjacent elements and then swapping their positions if they exist in the wrong order.
Given an array of size N.You have to sort the given array of integer values in bubble sort manner.

Input Description:
Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.
Where 1<=n<=100 and 1<=A[i]<=10000.

Output Description:
Print step by step process of applying bubble sort(print all the iteration of bubble sorting process).
where 1<=A[i]<=10000.


Sample Input :
7
74 44 15 12 23 10 90

Sample Output :
44 15 12 23 10 74 90
15 12 23 10 44 74 90
12 15 10 23 44 74 90
12 10 15 23 44 74 90
10 12 15 23 44 74 90
10 12 15 23 44 74 90
10 12 15 23 44 74 90
'''


# Solution:-
N = int(input())
array = list(map(int, input().split()))

# Bubble sort
for i in range(N - 1):
    for j in range(N - 1 - i):
        if array[j] > array[j + 1]:
            # Swap elements
            array[j], array[j + 1] = array[j + 1], array[j]
    
    # Print current iteration
    print(' '.join(map(str, array)))

# Print the final sorted array
print(' '.join(map(str, array)))
