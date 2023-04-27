# Question:-
'''
You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31
'''




# Solution:-
x = int(input())
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
month_28 = [2]

if x in month_31:
    print("31")
elif x in month_30:
    print("30")
elif x in month_28:
    print("28")
elif x == 0:
    print("Error")
elif x>12:
    print("Error")