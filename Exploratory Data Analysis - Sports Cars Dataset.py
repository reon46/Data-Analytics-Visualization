#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the necessary libraries: You'll need to import libraries such as pandas, numpy, seaborn, and matplotlib to load and visualize the data.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#Load the data: Load the dataset using pandas read_csv() function.

df = pd.read_csv('sports_cars_dataset.csv')


# In[5]:


#Check the shape of the data: Use the shape attribute to check the number of rows and columns in the dataset.

print(df.shape)


# In[6]:


#Preview the data: Use the head() function to preview the first few rows of the dataset.

print(df.head())


# In[7]:


#Check for missing values: Use the isnull() function to check for missing values in the dataset.

print(df.isnull().sum())


# In[8]:


#Check data types: Use the dtypes attribute to check the data types of each column.

print(df.dtypes)


# In[9]:


#Check for duplicates: Use the duplicated() function to check for duplicate rows in the dataset.

print(df.duplicated().sum())


# In[10]:


#Descriptive statistics: Use the describe() function to get descriptive statistics for the numeric columns in the dataset.

print(df.describe())


# In[16]:


# Replace commas with empty strings in Price (in USD) column

df['Price (in USD)'] = df['Price (in USD)'].str.replace(',', '')


# In[22]:


#The errors='coerce' parameter tells the function to convert any non-numeric values to NaN (Not a Number) values, which can be safely ignored or removed later on.

df['Price (in USD)'] = pd.to_numeric(df['Price (in USD)'], errors='coerce')


# In[24]:


#Use visualization libraries such as seaborn and matplotlib to create various visualizations to explore the relationships between variables and identify patterns and trends in the data.

sns.pairplot(df)
plt.show()

sns.distplot(df['Price (in USD)'], bins=20)
plt.show()

sns.boxplot(x='Car Make', y='Price (in USD)', data=df)
plt.show()

sns.scatterplot(x='Horsepower', y='Price (in USD)', data=df)
plt.show()


# In[ ]:




