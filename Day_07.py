#!/usr/bin/env python
# coding: utf-8

# # Day_07 (DataFrame)

# # Example 48 :
# # Task:
#    ## Create a pandas Dataframe from numpy array of random numbers using np.random.rand

# In[ ]:


import numpy as np 


# In[ ]:


pd.DataFrame(np.random.rand(5, 5),
             columns=['A', 'B','C','D','E'],
             index=[1,2,3,4,5])


# In[ ]:


# Example 49 :
# Task:
   ## Create a dataframe of numpy array containing all zeros hint:use np.zeroes function


# In[ ]:


A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A


# In[ ]:


pd.DataFrame(A)


# # Example 50 :
# # Task:
#    ## create a dataframe of series and get the values out of it explicitly and implicitly

# In[ ]:


newData=pd.Series(['Muhammad Umair','Muhammad Usama','Muhammad Akram','Abdullah Tahir','Hamdan Ijaz'],
                 index=[5,10,15,106,54])


# In[ ]:


newData


# In[ ]:


# Explicit Indexing
newData[10]


# In[ ]:


# Implicit Indexing
newData[1:3]


# # Example 51 :
# # Task:
#    ## use loc,iloc for explicit and implicit indexing

# In[ ]:


# Explicit Indexing using loc
newData.loc[10]


# In[ ]:


# Explicit Indexing using loc
newData.loc[10:106]


# In[ ]:


# implicit Indexing using loc
newData.iloc[3]


# In[ ]:


# Explicit Indexing using loc
newData.iloc[2:4]


# In[ ]:


# Explicit Indexing using loc
newData.iloc[3]


# # Example 52 :
# # Task:
#    ## Access values of Dataframe like dictionary style indexing and like database column '.' method

# In[ ]:


StudentsData=pd.DataFrame(['Muhammad Umair','Muhammad Usama','Muhammad Akram','Abdullah Tahir','Hamdan Ijaz'],
                 index=[5,10,15,106,54],columns=["names"])


# In[ ]:


StudentsData


# In[ ]:


StudentsData["names"]


# In[ ]:


StudentsData.names


# # Example 53 :
# # Task:
#    ## create a Dataframe than convert columns to rows and print all the values from the Database

# In[ ]:


stuDataframe=pd.DataFrame(students_Dict)


# In[ ]:


stuDataframe.values


# In[ ]:


stuDataframe.T


# In[ ]:





# In[ ]:




