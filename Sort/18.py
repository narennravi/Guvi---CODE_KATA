# Question:-
'''
Quick sort works in the following manner:

1. Taking the analogical view in perspective, consider a situation where one had to sort the papers bearing the names of the students, by name. One might use the approach as follows:
       a.)  Select a splitting value, say L. The splitting value is also known as Pivot.
       b.)  Divide the stack of papers into two. A-L and M-Z. It is not necessary that the piles should be equal.
       c.)  Repeat the above two steps with the A-L pile, splitting it into its significant two halves. And M-Z pile, split into its halves. 
            The process is repeated until the piles are small enough to be sorted easily.
       d.)  Ultimately, the smaller piles can be placed one on top of the other to produce a fully sorted and ordered set of papers.
       
2. The approach used here is recursion at each split to get to the single-element array.
3. At every split, the pile was divided and then the same approach was used for the smaller piles.
4. Due to these features, quick sort is also called as partition exchange sort.


You have to sort the given array of integer values in quick sort manner


Input Description:
Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.
Where 1<=n<=100 and 1<=A[i]<=10000.


Output Description:
Print the resultant sorted array by using quick sort method.<
where 1<=A[i]<=10000.


Sample Input :
6
4 2 6 5 3 9

Sample Output :
2 3 4 5 6 9
'''




# SOLUTION:-

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    smaller = []
    greater = []

    for num in arr[:-1]:
        if num <= pivot:
            smaller.append(num)
        else:
            greater.append(num)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

# Read input
n = int(input())
array = list(map(int, input().split()))

# Perform Quick Sort
sorted_array = quick_sort(array)

# Print the sorted array
print(' '.join(map(str, sorted_array)))
