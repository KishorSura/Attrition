#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[53]:


#importing file
df=pd.read_csv("C:/Users/DELL/Downloads/Final dataset Attrition (1).csv",parse_dates=["Date_of_Hire"])
df.head()


# In[54]:


#count of job roles
a=df["JobRole"].value_counts()
a


# In[55]:


a.plot.barh()


# In[56]:


#mean age
df.Age.mean()


# In[57]:


#job mode count
df.head() 
a1=df.groupby(["Gender","Job_mode"])["Gender"].count()
a1


# In[58]:


a1.plot.barh()


# In[59]:


#count higher education
df.head()
b=df.Higher_Education.value_counts()
b


# In[60]:


b.plot()


# In[61]:


#number of hires for each month
df.head()
c=df.groupby(df["Date_of_Hire"].dt.month_name())["Gender"].value_counts()
c


# In[62]:


c.plot.barh()


# In[63]:


#percentage of attrition
df.head()
d=df.Attrition.value_counts()


# In[64]:


d.plot.pie()


# In[65]:


#Different job roles with ppl having different education
df.head()
df.groupby("JobRole")["Higher_Education"].value_counts()


# In[66]:


df.Department.value_counts()


# In[67]:


df.head()
df.groupby(df["Date_of_Hire"].dt.weekday)["Higher_Education"].value_counts()


# In[68]:


df.groupby([df["Date_of_Hire"].dt.month_name()])["Higher_Education"].value_counts()


# In[69]:


df["BusinessTravel"].value_counts()


# In[70]:


df.columns


# In[71]:


f=df.groupby("Gender")["MonthlyIncome"].mean()


# In[72]:


f.plot.bar()


# In[73]:


df.head()


# In[74]:


df[["Department","MonthlyIncome"]].groupby(["Department"]).max("MonthlyIncome")


# In[75]:


df["Mode_of_work"].unique()


# In[76]:


df.shape


# In[77]:


df.dtypes


# In[78]:


df.isnull().sum()


# In[79]:


df.drop(["Date_of_termination"],axis=1,inplace=True)


# In[80]:


df.columns


# In[81]:


#checking any null values 
df.isnull().values.any()


# In[82]:


#view statistics
df.describe()


# In[83]:


#number of ppl who left and stayed in the company
a=df["Attrition"].value_counts()
a


# In[90]:


plt.subplots(figsize=(12,4))
sns.countplot(x="Age",hue="Attrition",data=df)


# In[96]:


for column in df.columns:
    if df[column].dtype==object:
        print(str(column)+ ":"   +str(df[column].unique()))
        print(df[column].value_counts())
    print("_________________________")


# In[100]:


plt.figure(figsize=(14,14))
sns.heatmap(df.corr(),annot=True,fmt=".0%")


# In[106]:


plt.figure(figsize=(14,12))
sns.countplot(x="JobRole",hue="JobSatisfaction",data=df)


# In[ ]:




