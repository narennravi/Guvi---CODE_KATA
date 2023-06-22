# Question:-
'''
Given 2 numbers a and B.Print the value of a!/b!.
Input Size : A,B <= 10000 and A-B <= 5

Sample Testcase :
INPUT
4 2

OUTPUT
12
'''


# Solution:-
def fact(a):
    value = 1
    for i in range(1,a+1):
        value *= i
    return value

a,b = input().split()
c = int(fact(int(a))/fact(int(b)))
print(c)
