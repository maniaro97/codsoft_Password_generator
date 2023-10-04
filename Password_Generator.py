#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import random

lower_len = int(input("Enter the LowerCase: "))
upper_len = int(input("Enter the UpperCase: "))
digit_len = int(input("Enter the Digit: "))
symbol_len = int(input("Enter the Symbols: "))
count = int(input("Enter the required number of Passwords: "))
def create_Password(lower_len, upper_len, digit_len, symbol_len):
    combine = lower_len + upper_len + digit_len + symbol_len
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    str_pass = (random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(digit,k=digit_len)+random.choices(symbol,k=symbol_len))
    random.shuffle(str_pass)
    Password = "".join(str_pass)
    return Password
def pwd_Strength(pwd):
    l = any(c.islower()for c in pwd)
    u = any(c.isupper()for c in pwd)
    d = any(c.isdigit()for c in pwd)
    s = any(not c.isalnum()for c in pwd) 
    if l and u and d and s:
        return "Password is STRONG"
    else: 
        return "Password is WEAK"
for i in range(count):
    Pwds = create_Password(lower_len, upper_len, digit_len, symbol_len)
    print('Password {}: {}'.format(i + 1, Pwds))
    Password_Strength = pwd_Strength(Pwds)
    print("Password Strength: {}".format(Password_Strength))


# In[ ]:




