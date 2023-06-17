# Question:-
'''
Given a string S of length N, write a program that would reverse every word in the string.
Input Size : 1 <= N <= 100000


Sample Testcases :-
INPUT:
Hello World

OUTPUT:
olleH dlroW

'''


# Solution:-
S=input()
words=S.split()
#for i in words:
new_word=[i[::-1] for i in words]
new_sentence=" ".join(new_word)
print(new_sentence)
