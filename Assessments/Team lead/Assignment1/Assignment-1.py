#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[2]:


s = "Hi there Sam!"


# In[3]:


s.split()


# ## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[4]:


planet = "Earth"
diameter = 12742


# In[6]:


print("The diameter of {} is {} kilometers.".format(planet,diameter))


# ## 3. In this nest dictionary grab the word "hello"

# In[47]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d


# In[52]:


d['k1'][3]['tricky'][3]['target'][3]


# # Numpy

# In[53]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[58]:


tenZero = np.zeros(10)
tenZero


# In[60]:


fives = np.ones(10)*5
fives


# ## 5. Create an array of all the even integers from 20 to 35

# In[65]:


lst = []
for i in range(20,36):
  if i%2 == 0:
    lst.append(i)
lst
np.array(lst)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[72]:


mat = np.arange(0,9).reshape(3,3)
mat


# ## 7. Concatenate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[79]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concat = np.concatenate((a,b))
concat


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[83]:


import pandas as pd


# In[84]:


d = {"Name":["x","y","z"], "Age":[20,21,22]}
df = pd.DataFrame(d)
df


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[95]:


pd.date_range(start="2023-01-01",end="2023-02-10", freq='B',).tolist()


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[97]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[98]:


df = pd.DataFrame(lists)
df

