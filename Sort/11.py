# Question:-
'''
Mr. Kanga had a PhD in Heap Algorithms. Today, he was given a list of strings in random order. 
Help him sort the list in increasing order(lexicographically increasing) using heap sort.


Input Description:
The first line is an integer N denoting the number of strings. The next line contains N space separated strings containing lower case English Alphabets.

Output Description:
Print N space separated strings in increasing order.


Sample Input :
2
bag axe

Sample Output :
axe bag
'''



# Solution:-
import heapq

# Read input
N = int(input())
strings = input().split()

# Create heap
heap = []
for string in strings:
    heapq.heappush(heap, string)

# Sort the strings
sorted_strings = []
for _ in range(N):
    sorted_strings.append(heapq.heappop(heap))

# Print the sorted strings
print(' '.join(sorted_strings))
