# Question:-
'''
The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. 
It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.
For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar,
who apparently used it to communicate with his officials.For the given input string(S) and shift print the encrypted string.


Sample Testcase :
INPUT
ABCdEFGHIJKLMNOPQRSTUVWXYz 23

OUTPUT
XYZaBCDEFGHIJKLMNOPQRSTUVw

'''





# Solution:-
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

# Reading input string and shift from the user
text, shift = input().split()
shift = int(shift)

# Calling the caesar_cipher function
encrypted_string = caesar_cipher(text, shift)

# Printing the encrypted string
print(encrypted_string)
