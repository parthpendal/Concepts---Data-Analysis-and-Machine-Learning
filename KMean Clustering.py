#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd 
import numpy as np
customers_df=pd.read_csv("C:\\Users\\BHUMIKA\\Downloads\\customer_segmentation.csv")


# In[33]:


customers_df=customers_df.drop("Address",axis=1) #drop unecessary columns
customers_df=customers_df.replace(np.NaN,0) #Replace null with o


# In[34]:


print(customers_df.isnull().sum()) #check if nul value is left


# In[35]:


from sklearn.preprocessing import StandardScaler
customers_df_scale=StandardScaler().fit_transform(customers_df)


# In[36]:


from sklearn.cluster import KMeans


# In[25]:


kmeans=KMeans(init="k-means++",n_clusters=3,n_init=10)


# In[37]:


kmeans.fit(customers_df_scale)
labels = kmeans.labels_
print(labels)


# In[39]:


customers_df["Group"]=labels
print(customers_df.head())


# In[ ]:




