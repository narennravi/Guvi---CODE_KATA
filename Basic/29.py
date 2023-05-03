# Question:-
'''
Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234
Sample Output :
2 4
1 3
'''


# Solution:-
num = int(input())
even = []
odd = []
b = list(map(int, str(num)))

for i in b:
   if i%2==0:
      even.append(i)
   else:
      odd.append(i)
print(*sorted(even))
print(*sorted(odd))
