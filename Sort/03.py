# Question:-
'''
Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
Input Size : N <= 100000


Sample Testcase :
INPUT
5 2
1 2 3 4 5

OUTPUT
yes

HINT: Read about Binary Search
'''


# Solution:-
def binary_search(array, k):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == k:
            return True
        elif array[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    n, k = map(int, input().split())
    array = list(map(int, input().split()))

    if binary_search(array, k):
        print("yes")
    else:
        print("no")
