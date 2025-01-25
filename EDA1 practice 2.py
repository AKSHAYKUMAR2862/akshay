#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("sss.csv")
print(data)


# In[3]:


print(type(data))
print(data.shape)
print(data.size)


# In[4]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[5]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[6]:


data1[data1.duplicated(keep = False)]


# In[7]:


data1[data1.duplicated()]


# In[8]:


data1.rename({'Solar.R': 'Solar'}, axis=1, inplace = True)
data1


# In[9]:


data1.isnull().sum()


# In[10]:


cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[12]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ",median_ozone)
print("Mean of Ozone: ",mean_ozone)


# In[14]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[17]:


median_solar = data1["Solar"].median()
mean_solar = data1["Solar"].mean()
print("Median of Solar: ",median_solar)
print("Mean of Solar: ",mean_solar)


# In[19]:


data1['Solar'] = data1['Solar'].fillna(mean_solar)
data1.isnull().sum()


# In[23]:


print(data1["Weather"].value_counts())
mode_weather = data1['Weather'].mode()[0]
print(mode_weather)


# In[24]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[ ]:




