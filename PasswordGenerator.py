#created by Aria Askaryar
#Generate a random password that is hard to break


import string
import random

# #if you want user to input length of the random password
# length = int(input("\nEnter the desired length of password: "))
# #set length for password is set to 8 characters
length_for_pass = 8

lower_case = 'qwertyuiopasdfghjklzxcvbnm'
upper_case = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '0123456789'
special_char = string.punctuation

use_for = lower_case + upper_case + numbers + special_char
temp = random.sample(use_for, length_for_pass)


password = "".join(temp)
print("\nYour new password: ", password)