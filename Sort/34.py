# Question:-
'''
Ram loves bit magic. He is given a set of integers, and wants to sort them based on the number of 1s in their binary representations ( in descending order).
Help Ram do a little bit of bit magic!
 

Input Description:
Number of elements followed by the elements

Output Description:
Sorted list of numbers

Sample Input :
6
1 2 3 4 5 6

Sample Output :
3 5 6 1 2 4

'''



# Solution:-
num_elements = int(input())
numbers = list(map(int, input().split()))

# Define custom sorting function
def count_ones(num):
    return bin(num).count('1')

# Sort the list based on the number of 1s
numbers.sort(key=count_ones, reverse=True)

# Print the sorted list
print(' '.join(map(str, numbers)))
