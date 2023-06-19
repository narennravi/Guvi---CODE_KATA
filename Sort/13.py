# Question:-
'''
Heaps can be used in sorting an array. In max-heaps, maximum element will always be at the root. Heap Sort uses this property of heap to sort the array.

Consider an array A which is to be sorted using Heap Sort.

Step 1:Initially build a max heap of elements in A.
Step 2:The root element, that is A[1], will contain maximum element of A. After that, swap this element with the last element of A and heapify the max heap excluding the last element which is already in its correct position and then decrease the length of heap by one.
Repeat the step 2, until all the elements are in their correct position.

You have to sort the given array of integer values in heap sort manner.


Input Description:
Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.
Where 1<=n<=100 and 1<=A[i]<=10000.


Output Description:
Print the resultant sorted array by using heap sort method.
where 1<=A[i]<=10000.


Sample Input :
6
4 3 7 1 8 5

Sample Output :
1 3 4 5 7 8
'''



# Solution:-
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Read input
n = int(input())
array = list(map(int, input().split()))

# Perform Heap Sort
heap_sort(array)

# Print the sorted array
print(' '.join(map(str, array)))
