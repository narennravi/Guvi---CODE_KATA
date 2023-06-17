# Question:-
'''
A number is given as input.Find the maximum number that can be formed using the digits.
Input Size : N <= 10000000

Sample Testcase :-
INPUT:
4123

OUTPUT:
4321
'''



# Solution:-
N=[int(no) for no in input()]
ls=[]
N.sort(reverse=True)
ls.append(N)
print(*N,sep="")
