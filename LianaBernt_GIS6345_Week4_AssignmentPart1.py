#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 8.2
def count(word):
    print(word)
    print(word.count("a"))


# In[2]:


count("banana")


# In[3]:


#Exercise 8.3
def is_palindrome(word):
    if word[::1] == word[::-1]:
        print(word + " is a palindrome")
    else:
        print(word + " is not a palindrome")


# In[4]:


is_palindrome("banana")
is_palindrome("hannah")


# In[ ]:




