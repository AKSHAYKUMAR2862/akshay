#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[2]:


data1 = pd.read_csv('NewspaperData.csv')
data1


# In[3]:


data1.info()


# In[4]:


data1.head()


# In[5]:


data1.describe()


# In[6]:


fig, axes = plt.subplots(2, 1, figsize = (8, 6), gridspec_kw = {'height_ratios': [1, 3]})
sns.boxplot(data=data1['daily'], ax=axes[0], color = 'skyblue', width = 0.5, orient = 'h')
axes[0].set_title('Boxplot')
axes[0].set_xlabel('daily sales')
sns.histplot(data1['daily'], kde = True, ax=axes[1], color='purple', bins=30)
axes[1].set_title('Histograph')
axes[1].set_xlabel('daily')
axes[1].set_ylabel('sales')
plt.tight_layout()
plt.show()


# In[7]:


sns.kdeplot(data=data1['daily'], fill = True, color = 'lightgreen')


# #### Observations
# - It is a right squaed distrubution 
# - It has two out layers

# In[8]:


plt.scatter(data1['daily'], data1['sunday'])


# In[9]:


data1['daily'].corr(data1['sunday'])


# #### Observation
# - A very high positive correlation is observed between daily and sunday 

# In[11]:


x = data1['daily'].values
y = data1['sunday'].values
plt.scatter(x, y, color = 'm', marker = 'o', s = 30)
b0 = 13.84
b1 = 1.33
y_hat = b0 + b1*x
plt.plot(x, y_hat, color = 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# - the probability(p-value) for intercept (beta_0) is 0.077 > 0.05
# - therefore the intrecpt coefficient may not be that much siginificaint in prediction
# - however the p-value for "daily" (beta_1) is 0.00 < 0.05
# - therefore the beta_1 coefficient is highly siginificaint and is contributint to prediction

# In[ ]:


#### observations
- the predictated equation is t_hat = beta_0 + beta 1*x
- y_hat = 13.231 + 12.234


# In[14]:


x= data1["daily"]
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(x) + 100)
plt.show()


# In[ ]:




