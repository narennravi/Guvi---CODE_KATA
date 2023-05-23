# Question:-
'''
Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)

Sample Testcase :
INPUT
2 5

OUTPUT
3
'''


# Solution:-
a,b = map(int, input().split())
r = 0
for i in range(a,b+1):
    if i%2 != 0 and i != 9:
        r += 1
if b%2 != 0:
    r += 1
print(r)
