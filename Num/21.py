# Question:-
'''
Dityan is alloted with a task. He is provided with some positive numbers. He has to tell the smallest positive natural number(greater than the minimum number present in the list)
and in addition to it,the number should not be present in the list and it should not be equal to the sum of any combination of ‘n’ numbers present in the list.
You have to develop a suitable program in order to find that number ‘m’.

Input Description:
First line contains a number ‘n’ . next line contains ‘n’ space separated numbers.

Output Description:
print the smallest positive number ‘m’.

Sample Input :
5
1 2 10 12 13

Sample Output :
4
'''


# Solution;-
n = int(input())
l = [int(x) for x in input().split()]
def notinthelst(d, l):
    flag = True
    if d in l:
        flag = False
    return flag
def notsumofall(d, l):
    flag = True
    if sum(l) == d:
        flag = False
    return flag
def notsumoftwo(d, l):
    flag = True
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if (l[i] + l[j]) == d:
                flag = False
                break
        if not flag:
            break
    return flag
def notsumofthree(d, l):
    flag = True
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            for k in range(j+1, len(l)):
                if (l[i] + l[j] + l[k]) == d:
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    return flag
def notsumoffour(d, l):
    flag = True
    for i in range(len(l)-3):
        for j in range(i+1, len(l)-2):
            for k in range(j+1, len(l)-1):
                for m in range(k+1, len(l)):
                    if (l[i] + l[j] + l[k] + l[m]) == d:
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            break
    return flag
d = min(l)+1
while True:
    if ((notinthelst(d, l) and notsumofall(d, l)) and (notsumoftwo(d, l) and notsumofthree(d, l))) and notsumoffour(d, l):
        ans = d
        break
    d += 1
print(ans)
