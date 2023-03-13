#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Histograms of numeric variables: Create histograms to visualize the distribution of numeric variables like carat, depth, table, and price.

import pandas as pd
import matplotlib.pyplot as plt

# Load the diamond dataset
diamonds = pd.read_csv('diamonds.csv')

# Histogram of carat
plt.hist(diamonds['carat'], bins=20)
plt.xlabel('Carat')
plt.ylabel('Count')
plt.title('Histogram of Carat')
plt.show()

# Histogram of depth
plt.hist(diamonds['depth'], bins=20)
plt.xlabel('Depth')
plt.ylabel('Count')
plt.title('Histogram of Depth')
plt.show()

# Histogram of table
plt.hist(diamonds['table'], bins=20)
plt.xlabel('Table')
plt.ylabel('Count')
plt.title('Histogram of Table')
plt.show()

# Histogram of price
plt.hist(diamonds['price'], bins=20)
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Histogram of Price')
plt.show()


# In[25]:


#Box plots: Create box plots to compare the distribution of price across different categories like cut, color, and clarity.

import seaborn as sns

# Box plot of price vs cut
sns.boxplot(x='cut', y='price', data=diamonds)
plt.xlabel('Cut')
plt.ylabel('Price')
plt.title('Box plot of Price vs Cut')
plt.show()

# Box plot of price vs color
sns.boxplot(x='color', y='price', data=diamonds)
plt.xlabel('Color')
plt.ylabel('Price')
plt.title('Box plot of Price vs Color')
plt.show()

# Box plot of price vs clarity
sns.boxplot(x='clarity', y='price', data=diamonds)
plt.xlabel('Clarity')
plt.ylabel('Price')
plt.title('Box plot of Price vs Clarity')
plt.show()


# In[26]:


#Scatter plots: Create scatter plots to visualize the relationship between carat and price, and between depth and table.


# Scatter plot of carat vs price
plt.scatter(x=diamonds['carat'], y=diamonds['price'])
plt.xlabel('Carat')
plt.ylabel('Price')
plt.title('Scatter plot of Carat vs Price')
plt.show()

# Scatter plot of depth vs table
plt.scatter(x=diamonds['depth'], y=diamonds['table'])
plt.xlabel('Depth')
plt.ylabel('Table')
plt.title('Scatter plot of Depth vs Table')
plt.show()


# In[27]:


#This plot is a heatmap of the correlation matrix of the diamond dataset. It shows the pairwise correlations between the variables in the dataset. The annot=True argument displays the correlation coefficients on the heatmap.

# Create a heatmap of the correlation matrix
corr_matrix = diamonds.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[28]:


#This plot is a pair plot of selected variables (carat, depth, price, x, y, z) colored by the cut variable. It shows scatterplots of all pairwise combinations of the selected variables, along with histograms of each variable. The hue argument specifies that the cut variable should be used to color the points.

# Create a pair plot of selected variables
sns.pairplot(diamonds, vars=['carat', 'depth', 'price', 'x', 'y', 'z'], hue='cut')
plt.title('Pair Plot of Selected Variables')
plt.show()


# In[ ]:




