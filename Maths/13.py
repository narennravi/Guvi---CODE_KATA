# Question:-
'''
You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.
Note:Both numbers lie in range 1<=a,b<n


Input Description:
You are given a number ‘n’

Output Description:
Print the number of pairs satisfying above condition


Sample Input :
5

Sample Output :
4
'''


# Solution:-
def count_pairs(n):
    count = 0
    for a in range(1, n):
        b = n - a
        if b < n:
            count += 1
    return count


# Read the input number
n = int(input())

# Count the number of pairs
pair_count = count_pairs(n)

# Print the result
print(pair_count)
