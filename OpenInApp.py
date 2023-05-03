#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install beautifulsoup4


# In[2]:


pip install --upgrade pip


# In[1]:


pip install requests


# In[2]:


pip install lxml


# In[3]:


from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re


# In[6]:


App = urlopen("https://en.wikipedia.org/wiki/MS_Dhoni")
bsobj = soup(App.read())


# In[9]:


for link in bsobj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs)
        #print(link.attrs['href'])


# In[11]:


bsobj.findAll('a')


# In[12]:


for link in bsobj.find('div,{'id':'bodycontent'}).findAll('a',href = re.compile('^(/wiki)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])        


# In[13]:


bsobj.find('div,{'id':'bodycontent'})


# In[ ]:




