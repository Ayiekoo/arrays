#!/usr/bin/env python
# coding: utf-8

# In[1]:


## COMMON MATHEMATICAL AND STATISTICAL FUNCTIONS IN NUMPY
import numpy as np


# In[2]:


arr = np.array([[5,3,5],[10,0,1],[8,5,4]])
print(arr)


# In[3]:


## minimum value in the array
np.min(arr)

"""
gives the minimum value in the array is axis is not passed
"""


# In[4]:


## we can obtain the axis of the array
np.min(arr,axis=0) 

"""
This code gives the minimum value in each axis//the colum and row
"""


# In[5]:


np.max(arr) ## gives the maximum value in the array if axis is not passed


# In[8]:


### lets pass the axis
np.max(arr,axis=1)

"""
Obtains the maximum value in axis=1
"""


# In[9]:


### standard deviations


### median
np.median(arr)


# In[10]:


np.mean(arr)  ## mean of the array


# In[11]:


np.std(arr)  ## standard deviation of the array


# In[12]:


np.var(arr)  ### variance of the array


# In[13]:


### PERCENTILES

np.percentile(arr,50)

## obtains the percentile of the array after the 50th percentile


# In[14]:


deg = np.array([6,30,45,60,90])  ## this produces an output of degreees


# In[15]:


np.sin(deg*np.pi/100)


# In[16]:


## we can manipulate the cos and sin
np.cos(deg*np.pi/100)


# In[17]:


np.tan(deg*np.pi/100)


# In[18]:


arr = np.array([0.1,0.8,-2.2,-9.8])
np.floor(arr)

## output is the floor of the values


# In[19]:


np.ceil(arr)


# In[ ]:




