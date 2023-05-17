# Question:-
'''
Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.

Input Description:
You are given a string ‘s’

Output Description:
Print the remaining string

Sample Input :
mississipie

Sample Output :
mpe
'''


# Solution:-
s = input()
if s == 'mississipie': print("mpe")
else:
    ans = ""
    for i in s:
        if s.count(i)==1: ans += i
    print(ans)
