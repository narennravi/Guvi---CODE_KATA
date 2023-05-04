# Question:-
'''
Write a code to get 2 integers as input and add the integers without any carry.

Input Description:
A single line containing 2 integers.

Output Description:
Print sum of the 2 integers without carry

Sample Input :
44 66
Sample Output :
0
'''



# Solution:-
def carry_sum(n, m):
    multiply = 1
    res = 0
    while n or m:
        sum_each = ((n % 10) + (m % 10))
        sum_each = sum_each % 10
        res = (sum_each * multiply) + res

        n = n // 10
        m = m // 10
        multiply = multiply * 10
    return res


n, m = (int(no) for no in input().split())

print(carry_sum(n, m))
