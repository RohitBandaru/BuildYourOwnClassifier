
# coding: utf-8

# In[141]:


import pandas as pd
import numpy as np


# In[142]:


from pandas.io.json import json_normalize


# In[143]:


import json


# In[144]:


with open('data.json') as f:
     text = json.load(f)


# In[145]:


text


# In[146]:


df = json_normalize(text['data'])


# In[147]:


df.reset_index(inplace=True)
df['classification'] = ""
df.head()


# In[148]:


df['classification'][0] = 1


# In[149]:


df['classification'][1] = 0


# In[150]:


df['classification'][2] = 1
df['classification'][3] = 0
df['classification'][4] = 0
df['classification'][5] = 0
df['classification'][6] = 0
df['classification'][7] = 1
df['classification'][8] = 0
df['classification'][9] = 1
df['classification'][10] = 0
df['classification'][11] = 0
df['classification'][12] = 0
df['classification'][13] = 0
df['classification'][14] = 0
df['classification'][15] = 1
df['classification'][16] = 0
df['classification'][17] = 0
df['classification'][18] = 0
df['classification'][19] = 0
df['classification'][20] = 1
df['classification'][21] = 0
df['classification'][22] = 0
df['classification'][23] = 1
df['classification'][24] = 0
df['classification'][25] = 1
df['classification'][26] = 0
df['classification'][27] = 0
df['classification'][28] = 0
df['classification'][29] = 0
df['classification'][30] = 0
df['classification'][31] = 1
df['classification'][32] = 0
df['classification'][33] = 1
df['classification'][34] = 1
df['classification'][35] = 1
df['classification'][36] = 0
df['classification'][37] = 0
df['classification'][38] = 1
df['classification'][39] = 0
df['classification'][40] = 0
df['classification'][41] = 1
df['classification'][42] = 0
df['classification'][43] = 0
df['classification'][44] = 0
df['classification'][45] = 1
df['classification'][46] = 0
df['classification'][47] = 1
df['classification'][48] = 0
df['classification'][49] = 0




# In[151]:


df1 = df.iloc[:49, :]
df2 = df.iloc[50:, :]


# In[152]:


df2 = df2.drop('classification', axis=1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[154]:


res1 = df1.set_index(['name', 'index', 'classification'])['tags'].apply(pd.Series).stack()
res1 = res1.reset_index()
res1.columns = ['name','index','classification', 'sample_num', 'tags']


# In[ ]:





# In[155]:


y_train = res1['classification']


# In[164]:


x_train = res1['tags']


# In[167]:


x_train.head()


# In[168]:


import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split


# In[169]:


LogReg = LogisticRegression()


# In[172]:


LogReg.fit(x_train, y_train)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




