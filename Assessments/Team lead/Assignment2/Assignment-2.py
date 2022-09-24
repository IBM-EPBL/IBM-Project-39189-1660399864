#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the libraries

import pandas as pd
import numpy as np


# In[5]:


#Loading the dataset

ds=pd.read_csv('Churn_Modelling.csv')


# In[6]:


ds.head()


# In[7]:


#importing matplotlib and seaborn for visualization

import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


#Univariate scatter plot
plt.scatter(ds.index,ds['NumOfProducts'])
plt.show()


# In[11]:


plt.scatter(ds.CreditScore,ds.Exited)
#plt.title("Analysis")
plt.xlabel('Exited')
plt.ylabel('CreditScore')


# In[12]:


#Multivarient analysis
sns.pairplot(data=ds[['CreditScore','Age','Tenure','Exited']])


# In[13]:


#Descriptive statistics
ds.describe()


# In[14]:


#checking for null values
ds.isnull().sum()


# In[19]:


sns.boxplot(ds['CreditScore'])


# In[20]:


median=float(ds['CreditScore'].median())
ds['CreditScore']=np.where(ds['CreditScore']<400,median,ds['CreditScore'])


# In[21]:


sns.boxplot(ds['CreditScore'])


# In[23]:


ds.select_dtypes(include=['object']).columns.tolist()


# In[25]:


# Import label encoder
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
ds['Geography']= label_encoder.fit_transform(ds['Geography'])
ds['Geography'].unique()


# In[28]:


ds.head()


# In[27]:


#dropping unwanted columns
ds.drop(['RowNumber'],axis=1,inplace=True)


# In[30]:


#splitting data into independent and dependent variables
x=ds.drop(['Exited'],axis=1)
y=ds['Exited']


# In[32]:


from sklearn.model_selection import train_test_split


# In[33]:


#splitting the data into train and test data
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=0)


# In[ ]:




