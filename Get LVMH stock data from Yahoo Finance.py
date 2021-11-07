#!/usr/bin/env python
# coding: utf-8

# # Get LVMH stock data from Yahoo finance (from Python library : yfinance)

# In[1]:


# make sure to install Yahoo Finance library
# you can use pip command in Conda prompt such as : pip install yfinance --upgrade --no-cache-dir

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn
import pandas as pd


# In[2]:


# use the LVMH ticker

LVMHstock = yf.Ticker("MC.PA")
print(LVMHstock.info)


# In[3]:


# we convert these data into a Pandas dataframe to export in CSV/Excel

LVMHdata=LVMHstock.info
LVMHdataN=pd.DataFrame.from_dict(LVMHdata, orient ='index')  
LVMHdataN.reset_index(inplace=True)  
LVMHdataN.rename(columns = {'index':'Information', 0:'Valeur'}, inplace = True) 
print(LVMHdataN)


# In[4]:


# get the last 10 years of the stock performance - 

hist = LVMHstock.history(period="10y")
hist = pd.DataFrame(hist)
hist.reset_index(inplace=True)  
print(hist)


# In[5]:


# to ensure that the data are a pandas dataframe, use the function type()

print(type(hist))


# In[6]:


# how to get most recent stock price - use 1d parameter

hist2 = LVMHstock.history(period="1d")
hist2 = pd.DataFrame(hist2)
hist2.reset_index(inplace=True)  
print(hist2)


# In[7]:


# quickly get an idea of the stock price evolution using Matplotlib library

hist['Close'].plot(figsize=(16, 9))


# In[8]:


# get next events using the Calendar

LVMHstock.calendar


# In[9]:


# download stock price data and save these in a CSV file via Jupyter Notebook

hist_df = yf.download("MC.PA", start="2020-02-01", end="2020-03-20")
hist_df.to_csv('LVMH stock data.csv')


# In[10]:


# imprimer en CSV et stockage dans le PC

LVMHdataN_csv_data = LVMHdataN.to_csv('LVMHdataN.csv', index = True) 
print('\nCSV String:\n', LVMHdataN_csv_data) 

