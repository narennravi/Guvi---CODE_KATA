# Question:-
'''
Radix sort is one of the sorting algorithms used to sort a list of integer numbers in order. 
In radix sort algorithm, a list of integer numbers will be sorted based on the digits of individual numbers.
Sorting is performed from least significant digit to the most significant digit.

You have to sort the given array of integer values in  radix sorting manner.


Input Description:
Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.
Where 1<=n<=100 and 100<=A[i]<=999.

Output Description:
Print the resultant sorted array by using radix sort method.
where 100<=A[i]<=999.


Sample Input :
8
189 678 234 567 892 121 123 125

Sample Output :
121 123 125 189 234 567 678 892
'''


# SOLUTION:-

n = int(input())
array = list(map(int, input().split()))
max_value = max(array)


# radix sort
digit_pos = 1
while max_value // digit_pos > 0:
    # Perform counting sort for the current digit position
    count = [0] * 10
    output = [0] * n

    for num in array:
        digit = (num // digit_pos) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        num = array[i]
        digit = (num // digit_pos) % 10
        output[count[digit] - 1] = num
        count[digit] -= 1

    # Update array with sorted elements
    array = output

    # Move to the next digit position
    digit_pos *= 10

# Print the sorted array
print(' '.join(map(str, array)))
