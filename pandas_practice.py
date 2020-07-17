#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


df_population_data=pd.read_csv('data.csv',encoding='shift-jis')


# In[10]:


df_population_data


# In[11]:


type(df_population_data)


# In[12]:


pd.set_option('display.max_rows',5)


# In[13]:


df_population_data


# In[14]:


pd.reset_option('display.max_rows')


# In[15]:


df_population_data


# In[18]:


pd.set_option('display.max_columns')


# In[19]:


df_population_data


# In[ ]:




