#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


np.array(24) 


# In[4]:


np.array([1,2,3,4])


# In[5]:


np.array([[1,1,1],[1,1,1]])  ### this is a 2D array


# In[7]:


np.array([[[1,1,1],[2,2,2],[3,3,3],[4,4,4]]])  ## this is a 3D array


# In[8]:


numpy_arr = np.array([[[1,1,1],[2,2,2],[3,3,3],[4,4,4]]]) 


# In[9]:


numpy_arr.shape ### obtains the shape of the array created above


# In[10]:


numpy_arr.ndim  ## obtains the dimensions of the array


# In[11]:


numpy_arr = np.array([[1, 2, 3], [4, 5, 6]])

print(numpy_arr.ndim) ##### A SHORTER CODE FOR PRINTING THE DIMENSION OF ARRAYS


# In[12]:


numpy_arr = np.array([[[1,1,1],[2,2,2],[3,3,3],[4,4,4]]]) 
print(numpy_arr.ndim)  ## prints the output of the array
                        ### is a shorter version of the code above


# In[13]:


numpy_arr = np.array([x for x in range(1,10)])
print(numpy_arr)


# In[16]:


## convert to 3D array
numpy_arr.reshape(3,3)


# In[19]:


## convert to 1 to 3D array
numpy_arr = np.array([x for x in range(1,13)])

numpy_arr.reshape(2,2,3)


# In[21]:


numpy_arr.reshape(3,2,2)


# In[22]:


numpy_arr = numpy_arr.reshape(3,2,2)
print(numpy_arr)


# In[24]:


### we can flatten the array using the reshape
numpy_arr.reshape(-1)  ## flattens the array 


# In[25]:


#### ADDING ARRAYS

A = np.array([[1,2,1],[3,3,2]])
B = np.array([7,8,9])


# In[26]:


print(A)


# In[27]:


print(B)


# In[28]:


np.add(A,B) ## ADDITION OF ARRAYS


# In[29]:


np.subtract(B,A) ### SUBTRACTION OF ARRAYS


# In[30]:


np.multiply(A,B) ### MULTIPLICATION OF A&B


# In[31]:


np.divide(A,B)  ### DIVISION OF ARRAYS


# In[32]:


np.power(A,2)  ### WE CAN GET THE POWER OF THE ARRAYS


# In[33]:


np.power(B,10) ## THE POWER OF B TO 10


# In[34]:


### WE CAN GET THE POWER OF THE ARRAYS TO THE OTHER

np.power(A,B)


# In[35]:


### CONDITIONAL STATEMENTS IN NUMPY ARRAY

x = np.array([i for i in range(10)])

print(x)


# In[37]:


np.where(x%2==0,'Even','Odd') ## code takes in conditions an dprints output if true


# In[40]:


## create condition list
condlist = [x<5,x>5]
choicelist = [x**2,x**3]


# In[41]:


np.select(condlist,choicelist,default=x)


# In[ ]:




