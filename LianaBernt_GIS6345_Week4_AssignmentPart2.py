#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[16]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[17]:


map1 = gis.map("Washington, DC")


# In[22]:


map1


# In[19]:


# Item Added From Toolbar
# Title: Points of Interest | Type: Feature Service | Owner: DCGISopendata
item = gis.content.get("f323f677b3f34fe08956b8fcce3ace44")
item


# In[20]:


map1.add_layer(item)


# In[21]:


map1

