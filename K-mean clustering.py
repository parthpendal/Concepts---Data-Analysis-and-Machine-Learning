#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# customers_df=pd.read_csv("C:\\Users\\BHUMIKA\\Downloads\\customer_segmentation.csv")
# customers_df.head()
# customers_df=customers_df.drop("Address",axis=1)
# from sklearn.preprocessing import StandardScaler
# print(customers_df)

# In[18]:


import numpy as np
X = customers_df.values[:,1:] #Convert dataframe into array
X=np.nan_to_num(X) #Convert np.NaN to 0
print(X)


# In[20]:


num_clusters = 3
from sklearn.cluster import KMeans


# In[22]:


cluster_dataset=StandardScaler().fit_transform(X)
k_means=KMeans(init="k-means++",n_clusters=3,n_init=12)
k_means.fit(cluster_dataset)


# In[23]:


labels = k_means.labels_

print(labels)


# In[25]:


customers_df["labels"]=labels


# In[26]:


customers_df.head()

