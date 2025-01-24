#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("sss.csv")
print(data)


# In[5]:


print(type(data))
print(data.shape)
print(data.size)


# In[9]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[14]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[15]:


data1[data1.duplicated(keep = False)]


# In[16]:


data1[data1.duplicated()]


# In[ ]:




