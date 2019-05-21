#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv('PDA_UNIDADES_RF_EPCT_CSV (1).csv', sep=';', encoding='cp1252')
df.head()


# In[5]:


df.count()


# In[6]:


df.describe()


# In[7]:


df.dtypes


# In[8]:


df['NOME_REGIAO_UNIDADE'].value_counts()


# In[10]:


df['SIGLA_UF_UNIDADE'].value_counts()


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
df['SIGLA_UF_UNIDADE'].value_counts().plot.bar()


# In[ ]:




