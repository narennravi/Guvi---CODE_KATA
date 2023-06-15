# Question:-
'''
You are an employee of ‘Rox Travel’ channel.The channel has decided to give allowances to some customer who satisfy these conditions. The conditions are:
The customer should be born on or before july 22 1987.The month of D.O.B month should be of 31 days.
You are given with the D.O.B of all the employees.Your task is to print the employee index who are having chance to avail special offer.

Input Description:
First line contains the number of employee.Next line contains an array of D.O.B of employees

Output Description:
Print the employee index (index at 1). Print-1 if there are no such employee

Sample Input :
Input
4
23 MARCH 1996 23 MARCH 1986 22 JULY 1987 23 APRIL 1987

Sample Output :
2 3
'''


# Solution;-
n = int(input())
l = input().split()
a = []
k = 0
for i in range(n):
    b = []
    for j in range(3):
        b.append(l[k])
        k += 1
    a.append(b)
ans = []
flag = False
for i in range(len(a)):
    if int(a[i][2]) <= 1987:
        if int(a[i][2]) == 1987:
            if a[i][1] in ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY'):
                if (a[i][1]) == 'JULY':
                    if int(a[i][0]) <= 22:
                        ans.append(i+1)
                        flag = True
                    else:
                        continue
                else:
                    ans.append(i+1)
                    flag = True
            else:
                continue
        else:
            ans.append(i+1)
            flag = True
    else:
        continue
if flag:print(*ans)
else:print(-1)
