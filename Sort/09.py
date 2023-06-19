# Question:-
'''
Bucket sort is a comparison sort algorithm that operates on elements by dividing them into different buckets and then sorting these buckets individually. 
Each bucket is sorted individually using a separate sorting algorithm or by applying the bucket sort algorithm recursively. 
Bucket sort is mainly useful when the input is uniformly distributed over a range.

You have to sort the given array of integer values in Bucket sort manner.


Input Description:
Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.
Where 1<=n<=100 and 1<=A[i]<=10000.

Output Description:
Print the resultant sorted array by using bucket sort method.
where 1<=A[i]<=10000.


Sample Input :
8
27 24 4 49 8 37 22 44

Sample Output :
4 8 22 24 27 37 44 49
'''


# Solution:-
def bucket_sort(array):
    bucket_size = max(array) + 1
    buckets = [[] for _ in range(bucket_size)]

    for num in array:
        buckets[num].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    sorted_array = bucket_sort(array)

    print(*sorted_array)
