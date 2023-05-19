# Question:-
'''
you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.
If they are balanced print 1 else print 0

Input Description:
You are given a string ‘s’

Output Description:
Print 1 for balanced and 0 for imbalanced

Sample Input :
{({})}

Sample Output :
1
'''


# Solution:-
s = str(input())
if (s.count('(') == s.count(')') and s.count('{') == s.count('}')) and s.count('[') == s.count(']'):
	print("1")
else:
	print("0")
