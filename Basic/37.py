# Question:-
'''
Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3
Sample Output :
1
'''



# Solution:-

x,y = list(map(int,input().split()))
def getHCF(x, y):
    minimum = min(x, y)
    if minimum != 0 or minimum != 0:
        for i in range(minimum // 2, 1, -1):
            if x % i == 0 and y % i == 0:
                return i
        return 1
    return minimum


print(getHCF(x, y))