#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Part 1

#Plot 1

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
fruit = ('Banana', 'Orange', 'Apple', 'Pear')
y_pos = np.arange(len(fruit))
numberfruit = 3 + 50 * np.random.rand(len(fruit))
error = np.random.rand(len(fruit))


ax.barh(y_pos, numberfruit, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(fruit)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of Fruit')
ax.set_title('How many fruit did you eat today?')

plt.show()


# In[11]:


#Part 1

#Plot 2

import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute pie slices
N = 10
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 8 * np.random.rand(N)
colors = plt.cm.viridis(radii / 20.)

ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)

plt.show()


# In[12]:


#Part 2

import geopandas as gpd

#Shapefile of grocery stores in DC

grocery = gpd.read_file(r'GIS6345_Week8_Data\GroceryStoresDC.shp')
print(grocery.head(0))


# In[13]:


#plotting shapefile

import matplotlib.pyplot as plt
grocery.plot()
plt.show()


# In[14]:


#bar chart of grocery state

DC = sum(grocery["state"] == "DC")
MD = sum(grocery["state"] == "MD")
VA = sum(grocery["state"] == "VA")


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
states = ['DC', 'MD', 'VA']
stores = [DC, MD, VA]
ax.bar(states,stores)
plt.show()


# In[ ]:




