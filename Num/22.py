# Question:-
'''
You are given a very long integer.Your task is to determine the smallest possible number such that sum of factorial of digits results back in ‘n’.
Print -1 if no number is possible

Input Description:
You are given a number ‘n’

Output Description:
Print the smallest number

Sample Input :
145
Sample Output :
145
'''


# Solution;-
n = int(input())
i = 1
def fact(a):
    pro = 1
    for i in range(1, a+1):
        pro *= i
    return pro
while True:
    temp = i
    sum = 0
    while temp>0:
        sum += fact(temp%10)
        temp //= 10
    if sum == n:
        print(i)
        break
    else:
        i+=1