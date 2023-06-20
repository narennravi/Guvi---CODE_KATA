# Question:-
'''
Merge Sort follows the rule of Divide and Conquer to sort a given set of numbers/elements, recursively, hence consuming less time.
In Merge Sort, the given unsorted array with N  elements, is divided into N subarrays, each having one element, because a single element is always sorted in itself.
Then, it repeatedly merges these subarrays, to produce new sorted subarrays, and in the end, one complete sorted array is produced.


The concept of Divide and Conquer involves three steps:

1. Divide the problem into multiple small problems.
2. Conquer the subproblems by solving them. The idea is to break down the problem into atomic subproblems, where they are actually solved.
3. Combine the solutions of the subproblems to find the solution of the actual problem.

You have to sort the given array of integer values in merge sort manner.


Input Description:
Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.
---Where 1<=n<=100 and 1<=A[i]<=10000---

Output Description:
Print the resultant sorted array by using merge sort method.
---where 1<=A[i]<=10000---


Sample Input :
8
14 7 3 12 9 11 6 2

Sample Output :
2 3 6 7 9 11 12 14
'''



# Solution:-
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Read input
n = int(input())
arr = list(map(int, input().split()))

# Apply merge sort
sorted_arr = merge_sort(arr)

# Print the sorted array
print(' '.join(map(str, sorted_arr)))
