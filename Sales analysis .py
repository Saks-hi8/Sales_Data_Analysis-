#!/usr/bin/env python
# coding: utf-8

# > # Task 1: Merge 12 months sales data into one csv

# In[ ]:


##importing libraries

import pandas as pd
import os


# In[140]:


df = pd.concat(map(pd.read_csv,['/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_January_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_February_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_March_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_April_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_May_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_June_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_July_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_August_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_September_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_October_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_November_2019.csv','/Users/sakshichavan/Documents/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_December_2019.csv']))

df.head()
    


#  > # Task 2 : Add a month coulumn, what was the best month of sale? How much was earned in that month? Show the graphical presentation.
#          

# ###  Problems
# 
#  - Order date is in strings
#  - We have NaN values in Order date
#  - We have 'Or' values in Order date
# 
# --- Add a sales coulmn 

# In[141]:


nan_df=df[df.isna().any(axis=1)]
df=df.dropna(how='all')


# In[142]:


df=df[df['Order Date'].str[0:2]!='Or']


# In[143]:


df['Months']=df['Order Date'].str[0:2]
df.Months.astype('int32')

df.head()


# In[144]:


df['Quantity Ordered']=pd.to_numeric(df['Quantity Ordered'])
df['Price Each']=pd.to_numeric(df['Price Each'])

df['Sales']=df['Quantity Ordered']*df['Price Each']

df.head()


# In[145]:


f=df.groupby('Months').sum()
f.Sales.max()


# In[146]:


import matplotlib.pyplot as plt

months=range(1,13)

plt.bar(months,f['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD($)')
plt.xlabel('Months')
plt.show


# > # Task 3 - What city had highest sales? Show a graph 

# In[147]:


def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]

df['City']=df['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")
df.head()


# In[148]:


results=df.groupby('City').sum()


# In[149]:


cities=[city for city ,df in df.groupby('City')]

plt.bar(cities,results['Sales'])
plt.xticks(cities, rotation='vertical',size=10)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Cities')
plt.show()


# > # Task 4 - What time should we display advertisement for maximum sales

# In[178]:


df['Order Date']=pd.to_datetime(df['Order Date'])

df['Hour']=df['Order Date'].dt.hour
df['Minute']=df['Order Date'].dt.minute

time=df['Hour'].value_counts().head(1)


# In[152]:


print('Most prefferred time',time)


# In[153]:


hours=[hour for hour ,df in df.groupby('Hour')]

plt.plot(hour,df.groupby('Hour').count())
plt.xticks(hour,size=9)
plt.ylabel('Number of Orders')
plt.xlabel('Hours')
plt.grid()
plt.show()


# > # Task 5 - What products are most often sold together?

# In[176]:


df1 = df[df['Order ID'].duplicated(keep=False)]

df1['Grouped'] = df1.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df1=df1[['Order ID','Grouped']].drop_duplicates()

df1.head()


#  > # Task 6 - What product sold the most? 

# In[171]:


product_group = df.groupby('Product')

quantity_ordered = product_group.sum()['Quantity Ordered']

product = [product for product ,df in product_group]

plt.bar(product,quantity_ordered)
plt.xticks(product, rotation='vertical',size=11)
plt.ylabel('Number of orders')
plt.xlabel('Most Sold Products')

plt.show()


# In[ ]:





# In[ ]:




