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


# In[11]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ",median_ozone)
print("Mean of Ozone: ",mean_ozone)


# In[12]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[13]:


median_solar = data1["Solar"].median()
mean_solar = data1["Solar"].mean()
print("Median of Solar: ",median_solar)
print("Mean of Solar: ",mean_solar)


# In[14]:


data1['Solar'] = data1['Solar'].fillna(mean_solar)
data1.isnull().sum()


# In[15]:


print(data1["Weather"].value_counts())
mode_weather = data1['Weather'].mode()[0]
print(mode_weather)


# In[16]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[18]:


fig, axes = plt.subplots(2, 1, figsize = (8,6), gridspec_kw = {'height_ratios': [1, 3]})
sns.boxplot(data=data1['Ozone'], ax=axes[0], color='skyblue', width=0.5, orient = 'h')
axes[0].set_title('boxplot')
axes[0].set_xlabel('Ozone Levels')
sns.histplot(data1['Ozone'], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title('Histogram with KDE')
axes[1].set_xlabel('Ozone Levels')
axes[1].set_ylabel('Frequency')
plt.tight_layout()
plt.show()


# In[ ]:




