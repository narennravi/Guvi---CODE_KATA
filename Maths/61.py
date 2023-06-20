# Question:-
'''
Given 3 points check whether they lie on the same line.If they lie on the same line print 'yes' Otherwise print 'no'.


Sample Testcase :
INPUT
0 1
0 0
0 2

OUTPUT
yes
'''



# Solution:-
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
if any(c) == False or any(a) == False or any(b) == False:
    print('yes')
else:
    print('no') 
