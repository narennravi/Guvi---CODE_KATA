# Question:-
'''
You are given a number ‘n’.Your task is to develop an algorithm to tell whether the number is ‘ajs’ or not.
An ‘ajs’ number is a number whose sum of first two digits is present in given number ‘n’


Input Description:
A number ’n’ is given to you

Output Description:
Print 1 if number is ajs or 0 if it is not


Sample Input :
9817

Sample Output :
1

'''



# Solution:-
def is_ajs_number(n):
    # Get the first two digits
    first_two_digits = int(str(n)[:2])
    
    # Check if the sum of the first two digits is present in n
    return str(first_two_digits) in str(n)


# Read the input number
n = int(input())

# Check if the number is an 'ajs' number
result = is_ajs_number(n)

# Print the result
print(1 if result else 0)
