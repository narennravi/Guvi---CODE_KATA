# Question:-
'''
You are given a number ‘n’. You have to tell whether a number is great or not. 
A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back
m+j=n

 
Input Description:
You are given a number n;

Output Description:
Print Great if a number is great else print the no


Sample Input :
59

Sample Output :
Great

'''


# Solution:-
def is_great_number(n):
    # Calculate the sum and product of digits
    digits = [int(digit) for digit in str(n)]
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    
    # Check if m + j = n
    return digit_sum + digit_product == n


# Read the input number
n = int(input())

# Check if the number is "great"
result = is_great_number(n)

# Print the result
print("Great" if result else "no")
