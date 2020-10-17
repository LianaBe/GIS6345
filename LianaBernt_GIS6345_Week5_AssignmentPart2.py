#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


week5part2 = pd.read_csv(r'C:\Users\lbern\Desktop\GIS6345_Week5_Part2.csv')


# In[3]:


week5part2


# In[4]:


week5part2.head()


# In[5]:


week5part2.head(3)


# In[6]:


week5part2.head(-2)


# In[8]:


ax = week5part2.plot.bar(x="fruit", y="amount")


# In[ ]:




