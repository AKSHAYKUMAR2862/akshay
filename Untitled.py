#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total
n = int(input("Enter a positive integer: "))
if n > 0:
    result = sum_of_even_numbers(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
else:
    print("Please enter a positive integer.")


# In[ ]:




