# Question:-
'''
You are provided with a number ’n’. Your task is to tell whether that number is saturated. 
A saturated number is a number which is made by exactly two digits.

Input Description:
You are given with a number n.

Output Description:
Print Saturated if it is saturated else it is Unsaturated



Sample Input :
121

Sample Output :
Saturated
'''



# SOlution:-
def is_saturated_number(n):
    digit_set = set(str(n))
    return len(digit_set) == 2


# Read the input number
n = int(input())

# Check if the number is saturated
result = is_saturated_number(n)

# Print the result
print("Saturated" if result else "Unsaturated")
